#!/usr/bin/env python
"""
RAG System Test & Validation Script
Tests core RAG functions: extraction, chunking, embedding, retrieval
"""

import sys
import os
from pathlib import Path

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported."""
    print("=" * 60)
    print("TEST 1: Checking Dependencies")
    print("=" * 60)
    
    dependencies = {
        'numpy': 'NumPy for numerical operations',
        'PyPDF2': 'PDF extraction',
        'docx': 'DOCX extraction',
        'sentence_transformers': 'Text embeddings',
        'sklearn': 'Scikit-learn utilities',
    }
    
    missing = []
    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {module:25} - {description}")
        except ImportError as e:
            print(f"❌ {module:25} - MISSING")
            missing.append(module)
    
    if missing:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing)}")
        print("Install with: pip install -r requirements_rag.txt")
        return False
    
    print("\n✅ All dependencies installed!\n")
    return True


def test_text_chunking():
    """Test text chunking logic."""
    print("=" * 60)
    print("TEST 2: Text Chunking")
    print("=" * 60)
    
    from models import rag_helper
    
    # Test text
    test_text = """
    Cloud computing is the delivery of computing services—including servers, storage, databases, 
    networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer 
    faster innovation, flexible resources, and economies of scale.
    
    You typically pay only for cloud services you use, helping you lower operating costs, run 
    infrastructure more efficiently, and scale as business needs change.
    
    AWS provides a broad set of global cloud-based products. AWS EC2 provides scalable computing 
    capacity in the cloud. Amazon S3 stores and protects any amount of data for a range of use cases.
    """.strip()
    
    chunks = rag_helper.chunk_text(test_text, chunk_size=100, overlap=20)
    
    print(f"Original text length: {len(test_text)} characters")
    print(f"Number of chunks created: {len(chunks)}")
    print("\nChunk preview:")
    for i, chunk in enumerate(chunks[:3], 1):
        preview = chunk[:80].replace('\n', ' ') + "..."
        print(f"  Chunk {i}: {preview}")
    
    if len(chunks) > 0:
        print("\n✅ Text chunking works!\n")
        return True
    else:
        print("\n❌ Failed to create chunks\n")
        return False


def test_embeddings():
    """Test embedding generation."""
    print("=" * 60)
    print("TEST 3: Embedding Generation")
    print("=" * 60)
    
    try:
        from models import rag_helper
        
        test_texts = [
            "AWS provides cloud computing services.",
            "Python is a programming language.",
            "Databases store structured data."
        ]
        
        print(f"Generating embeddings for {len(test_texts)} texts...")
        embeddings = rag_helper.compute_embeddings(test_texts)
        
        print(f"Embedding shape: {embeddings.shape}")
        print(f"Embedding dimensions: {embeddings.shape[1]}")
        
        if embeddings.shape[1] == 384:
            print("✅ Embeddings generated successfully (384 dimensions)!\n")
            return True
        else:
            print(f"⚠️  Unexpected dimension: {embeddings.shape[1]} (expected 384)\n")
            return False
            
    except Exception as e:
        print(f"❌ Embedding generation failed: {e}\n")
        return False


def test_similarity():
    """Test cosine similarity calculation."""
    print("=" * 60)
    print("TEST 4: Similarity Calculation")
    print("=" * 60)
    
    import numpy as np
    from models import rag_helper
    
    # Create test vectors
    v1 = np.array([1, 0, 0], dtype=np.float32)
    v2 = np.array([1, 0, 0], dtype=np.float32)
    v3 = np.array([0, 1, 0], dtype=np.float32)
    
    sim_identical = rag_helper.cosine_similarity(v1, v2)
    sim_orthogonal = rag_helper.cosine_similarity(v1, v3)
    
    print(f"Similarity (identical vectors): {sim_identical:.4f} (expected: 1.0)")
    print(f"Similarity (orthogonal vectors): {sim_orthogonal:.4f} (expected: 0.0)")
    
    if 0.99 < sim_identical <= 1.0 and -0.01 < sim_orthogonal < 0.01:
        print("✅ Similarity calculation works correctly!\n")
        return True
    else:
        print("❌ Similarity calculation incorrect\n")
        return False


def test_database_connection():
    """Test database connectivity."""
    print("=" * 60)
    print("TEST 5: Database Connection")
    print("=" * 60)
    
    try:
        from database.db import fetch_one
        
        # Try a simple query
        result = fetch_one("SELECT 1 as test")
        
        if result and result.get('test') == 1:
            print("✅ Database connection successful!\n")
            return True
        else:
            print("❌ Database query returned unexpected result\n")
            return False
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("Make sure MySQL is running and configured in config.py\n")
        return False


def test_rag_tables():
    """Test if RAG tables exist in database."""
    print("=" * 60)
    print("TEST 6: RAG Database Tables")
    print("=" * 60)
    
    try:
        from database.db import fetch_all
        
        required_tables = [
            'material_chunks',
            'chunk_embeddings',
            'rag_query_logs',
            'material_processing_status'
        ]
        
        result = fetch_all("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_SCHEMA = 'lms_db'
        """)
        
        existing_tables = [row['TABLE_NAME'] for row in result]
        
        all_exist = True
        for table in required_tables:
            if table in existing_tables:
                print(f"✅ {table:35} exists")
            else:
                print(f"❌ {table:35} MISSING")
                all_exist = False
        
        if all_exist:
            print("\n✅ All RAG tables exist!\n")
            return True
        else:
            print("\n❌ Some tables missing. Run: mysql -u root -p lms_db < schema_rag.sql\n")
            return False
            
    except Exception as e:
        print(f"❌ Error checking tables: {e}\n")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 12 + "RAG SYSTEM VALIDATION TESTS" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    tests = [
        ("Dependencies", test_imports),
        ("Text Chunking", test_text_chunking),
        ("Embeddings", test_embeddings),
        ("Similarity", test_similarity),
        ("Database", test_database_connection),
        ("RAG Tables", test_rag_tables),
    ]
    
    results = {}
    for name, test_func in tests:
        try:
            results[name] = test_func()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}\n")
            results[name] = False
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} {name}")
    
    print("-" * 60)
    print(f"Result: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 RAG system is ready to use!")
        print("\nNext steps:")
        print("1. Faculty: Upload course materials (PDF/DOCX)")
        print("2. Students: Ask questions in AI Assistant")
        print("3. System: Automatically retrieves relevant materials")
        return 0
    else:
        print("\n⚠️  Some tests failed. Fix issues before using RAG.")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
