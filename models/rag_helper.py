"""
RAG (Retrieval-Augmented Generation) Module for Course Materials
Handles document processing, embedding, retrieval, and grounded AI responses
"""

import os
import json
import time
import re
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple, Optional

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    from docx import Document
except ImportError:
    Document = None

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

from database.db import fetch_all, fetch_one, execute_query

# ============================================================================
# CONFIGURATION
# ============================================================================

CHUNK_SIZE = 500  # Characters per chunk
CHUNK_OVERLAP = 100  # Character overlap between chunks
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Lightweight model for CPU
MIN_CHUNK_LENGTH = 50  # Minimum characters for a chunk to be useful
RETRIEVAL_TOP_K = 5  # Number of top similar chunks to retrieve
CONFIDENCE_THRESHOLD = 0.3  # Minimum similarity score to consider a match

# ============================================================================
# DOCUMENT PROCESSING
# ============================================================================

def extract_text_from_pdf(file_path: str) -> Dict[str, any]:
    """
    Extract text from a PDF file.
    Returns: {text: str, page_count: int, pages: [str]}
    """
    if not PyPDF2:
        return {"error": "PyPDF2 not installed. Install with: pip install PyPDF2"}
    
    try:
        extracted_data = {"text": "", "page_count": 0, "pages": []}
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            extracted_data["page_count"] = len(reader.pages)
            
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                extracted_data["pages"].append(text)
                extracted_data["text"] += f"\n--- Page {page_num} ---\n{text}"
        
        return extracted_data
    except Exception as e:
        return {"error": f"PDF extraction failed: {str(e)}"}


def extract_text_from_docx(file_path: str) -> Dict[str, any]:
    """
    Extract text from a DOCX file.
    Returns: {text: str, paragraphs: int}
    """
    if not Document:
        return {"error": "python-docx not installed. Install with: pip install python-docx"}
    
    try:
        doc = Document(file_path)
        extracted_data = {"text": "", "paragraphs": 0, "sections": []}
        
        for para in doc.paragraphs:
            if para.text.strip():
                extracted_data["text"] += para.text + "\n"
                extracted_data["paragraphs"] += 1
        
        return extracted_data
    except Exception as e:
        return {"error": f"DOCX extraction failed: {str(e)}"}


def extract_text_from_material(file_path: str) -> Dict[str, any]:
    """
    Intelligently extract text from PDF or DOCX based on file extension.
    """
    ext = Path(file_path).suffix.lower()
    
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        return extract_text_from_docx(file_path)
    else:
        return {"error": f"Unsupported file type: {ext}"}


# ============================================================================
# TEXT CHUNKING
# ============================================================================

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    """
    Split text into overlapping chunks for better context preservation.
    """
    chunks = []
    text = text.strip()
    
    if len(text) <= chunk_size:
        if len(text) > MIN_CHUNK_LENGTH:
            chunks.append(text)
        return chunks
    
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        
        # Try to break at a sentence boundary
        if end < len(text):
            # Look for last period, newline, or comma within chunk
            for boundary in ['. ', '.\n', '\n', ', ', ' ']:
                last_boundary = text.rfind(boundary, start, end)
                if last_boundary > start + MIN_CHUNK_LENGTH:
                    end = last_boundary + len(boundary)
                    break
        
        chunk = text[start:end].strip()
        if len(chunk) >= MIN_CHUNK_LENGTH:
            chunks.append(chunk)
        
        # Move start position with overlap
        start = end - overlap
    
    return chunks


# ============================================================================
# EMBEDDING & VECTOR STORAGE
# ============================================================================

def get_embedding_model():
    """Load the embedding model (lazy loading)."""
    if not SentenceTransformer:
        raise ImportError("sentence-transformers not installed. Install with: pip install sentence-transformers")
    return SentenceTransformer(EMBEDDING_MODEL)


def compute_embeddings(texts: List[str]) -> np.ndarray:
    """
    Compute embeddings for a list of text chunks.
    Returns: numpy array of shape (len(texts), embedding_dim)
    """
    model = get_embedding_model()
    embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    return embeddings


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return np.dot(a, b) / (norm_a * norm_b)


# ============================================================================
# DATABASE OPERATIONS
# ============================================================================

def store_chunk(material_id: int, course_id: int, chunk_text: str, chunk_index: int, 
                page_number: int = None, source_doc_name: str = None) -> int:
    """Store a text chunk in the database."""
    query = """
        INSERT INTO material_chunks 
        (material_id, course_id, chunk_index, chunk_text, page_number, source_doc_name, chunk_size)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    chunk_size = len(chunk_text)
    return execute_query(query, 
        (material_id, course_id, chunk_index, chunk_text, page_number, source_doc_name, chunk_size),
        return_lastrowid=True)


def store_embedding(chunk_id: int, embedding_vector: np.ndarray, model_name: str = EMBEDDING_MODEL) -> int:
    """Store embedding vector for a chunk."""
    query = """
        INSERT INTO chunk_embeddings (chunk_id, embedding_vector, embedding_model, embedding_dimension)
        VALUES (%s, %s, %s, %s)
    """
    # Convert numpy array to binary format for storage
    embedding_bytes = embedding_vector.astype(np.float32).tobytes()
    embedding_dim = len(embedding_vector)
    return execute_query(query, (chunk_id, embedding_bytes, model_name, embedding_dim), return_lastrowid=True)


def get_chunks_by_course(course_id: int) -> List[Dict]:
    """Retrieve all chunks for a course."""
    query = """
        SELECT mc.id, mc.chunk_text, mc.chunk_index, mc.page_number, 
               mc.source_doc_name, cm.title as material_title
        FROM material_chunks mc
        LEFT JOIN course_materials cm ON mc.material_id = cm.id
        WHERE mc.course_id = %s
        ORDER BY mc.material_id, mc.chunk_index
    """
    return fetch_all(query, (course_id,))


def get_embedding_for_chunk(chunk_id: int) -> Optional[np.ndarray]:
    """Retrieve embedding vector for a chunk."""
    query = """
        SELECT embedding_vector, embedding_dimension
        FROM chunk_embeddings
        WHERE chunk_id = %s
    """
    result = fetch_one(query, (chunk_id,))
    if result and result['embedding_vector']:
        # Convert binary back to numpy array
        embedding = np.frombuffer(result['embedding_vector'], dtype=np.float32)
        return embedding
    return None


def update_material_processing_status(material_id: int, status: str, chunk_count: int = 0, 
                                     error_msg: str = None, processing_time: int = None):
    """Update material processing status."""
    query = """
        INSERT INTO material_processing_status 
        (material_id, processing_status, chunk_count, error_message, processed_at, processing_time_seconds)
        VALUES (%s, %s, %s, %s, NOW(), %s)
        ON DUPLICATE KEY UPDATE
            processing_status = VALUES(processing_status),
            chunk_count = VALUES(chunk_count),
            error_message = VALUES(error_message),
            processed_at = NOW(),
            processing_time_seconds = VALUES(processing_time_seconds)
    """
    execute_query(query, (material_id, status, chunk_count, error_msg, processing_time))


# ============================================================================
# RAG PIPELINE
# ============================================================================

def process_course_material(material_id: int, course_id: int, file_path: str, 
                           material_title: str) -> Dict[str, any]:
    """
    Complete RAG pipeline: extract → chunk → embed → store.
    """
    start_time = time.time()
    update_material_processing_status(material_id, 'processing')
    
    try:
        # 1. Extract text
        extraction_result = extract_text_from_material(file_path)
        if "error" in extraction_result:
            update_material_processing_status(material_id, 'failed', error_msg=extraction_result['error'])
            return extraction_result
        
        text = extraction_result.get('text', '')
        pages = extraction_result.get('pages', [])
        
        if not text or len(text.strip()) < 100:
            update_material_processing_status(material_id, 'failed', error_msg='Document is empty or too short')
            return {"error": "Document is empty or too short"}
        
        # 2. Chunk text
        chunks = chunk_text(text)
        if not chunks:
            update_material_processing_status(material_id, 'failed', error_msg='No valid chunks created')
            return {"error": "No valid chunks created from document"}
        
        # 3. Compute embeddings
        embeddings = compute_embeddings(chunks)
        
        # 4. Store chunks and embeddings
        chunk_count = 0
        for chunk_idx, (chunk_text, embedding) in enumerate(zip(chunks, embeddings)):
            # Infer page number
            page_num = None
            if pages:
                cumulative_len = 0
                for page_idx, page_text in enumerate(pages, 1):
                    cumulative_len += len(page_text)
                    if cumulative_len >= len(text[:len(text.split(chunk_text)[0])]):
                        page_num = page_idx
                        break
            
            chunk_id = store_chunk(material_id, course_id, chunk_text, chunk_idx, 
                                  page_number=page_num, source_doc_name=material_title)
            store_embedding(chunk_id, embedding)
            chunk_count += 1
        
        # 5. Update status
        processing_time = int(time.time() - start_time)
        update_material_processing_status(material_id, 'completed', chunk_count=chunk_count, 
                                         processing_time=processing_time)
        
        return {
            "success": True,
            "material_id": material_id,
            "chunks_created": chunk_count,
            "processing_time_seconds": processing_time,
            "text_length": len(text),
            "pages": extraction_result.get('page_count', 'unknown')
        }
    
    except Exception as e:
        processing_time = int(time.time() - start_time)
        error_msg = f"Processing failed: {str(e)}"
        update_material_processing_status(material_id, 'failed', error_msg=error_msg, 
                                         processing_time=processing_time)
        return {"error": error_msg}


def retrieve_relevant_chunks(course_id: int, query: str, top_k: int = RETRIEVAL_TOP_K) -> List[Dict]:
    """
    Retrieve top-K most relevant chunks for a query using semantic similarity.
    """
    # Get all chunks for the course with their embeddings
    all_chunks = get_chunks_by_course(course_id)
    if not all_chunks:
        return []
    
    # Compute query embedding
    query_embedding = compute_embeddings([query])[0]
    
    # Score each chunk
    scored_chunks = []
    for chunk in all_chunks:
        chunk_id = chunk['id']
        chunk_embedding = get_embedding_for_chunk(chunk_id)
        
        if chunk_embedding is None:
            continue
        
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            **chunk,
            'similarity_score': float(similarity)
        })
    
    # Sort by similarity and filter by confidence threshold
    scored_chunks.sort(key=lambda x: x['similarity_score'], reverse=True)
    top_chunks = [c for c in scored_chunks[:top_k] if c['similarity_score'] >= CONFIDENCE_THRESHOLD]
    
    return top_chunks


def build_rag_context(retrieved_chunks: List[Dict]) -> Tuple[str, List[Dict]]:
    """
    Build context string from retrieved chunks and return sources.
    """
    if not retrieved_chunks:
        return "", []
    
    context = "COURSE MATERIAL CONTEXT:\n" + "=" * 50 + "\n\n"
    sources = []
    
    for chunk in retrieved_chunks:
        context += f"[Document: {chunk['material_title']}, Page {chunk['page_number'] or 'N/A'}]\n"
        context += chunk['chunk_text'] + "\n\n"
        
        sources.append({
            'document': chunk['material_title'],
            'page': chunk['page_number'],
            'chunk_id': chunk['id'],
            'confidence': chunk['similarity_score']
        })
    
    return context, sources


def log_rag_query(student_id: int, course_id: int, query: str, 
                 retrieved_chunk_ids: List[int], confidence_score: float, 
                 response_length: int, was_hallucination_prevented: bool):
    """Log RAG query for analytics."""
    query_result = """
        INSERT INTO rag_query_logs 
        (student_id, course_id, query, retrieved_chunk_ids, confidence_score, response_length, was_hallucination_prevented)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    chunk_ids_json = json.dumps(retrieved_chunk_ids)
    execute_query(query_result, 
        (student_id, course_id, query, chunk_ids_json, confidence_score, response_length, was_hallucination_prevented))
