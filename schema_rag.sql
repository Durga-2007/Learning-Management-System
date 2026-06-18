-- RAG Database Schema for Course Materials Processing

USE lms_db;

-- 1. Material Chunks Table (stores processed text chunks from materials)
CREATE TABLE IF NOT EXISTS material_chunks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT NOT NULL,
    course_id INT NOT NULL,
    chunk_index INT NOT NULL,
    chunk_text LONGTEXT NOT NULL,
    page_number INT,
    source_doc_name VARCHAR(255),
    chunk_size INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES course_materials(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    INDEX idx_course_id (course_id),
    INDEX idx_material_id (material_id)
);

-- 2. Embeddings Table (stores vector embeddings for semantic search)
CREATE TABLE IF NOT EXISTS chunk_embeddings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chunk_id INT UNIQUE NOT NULL,
    embedding_vector MEDIUMBLOB NOT NULL,
    embedding_model VARCHAR(100) DEFAULT 'all-MiniLM-L6-v2',
    embedding_dimension INT DEFAULT 384,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chunk_id) REFERENCES material_chunks(id) ON DELETE CASCADE,
    INDEX idx_chunk_id (chunk_id)
);

-- 3. RAG Query Log (tracks retrieval performance and student queries)
CREATE TABLE IF NOT EXISTS rag_query_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    query TEXT NOT NULL,
    retrieved_chunk_ids JSON,
    confidence_score DECIMAL(3, 2),
    response_length INT,
    was_hallucination_prevented BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    INDEX idx_student_course (student_id, course_id)
);

-- 4. Material Processing Status (tracks which materials have been processed)
CREATE TABLE IF NOT EXISTS material_processing_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT UNIQUE NOT NULL,
    processing_status ENUM('pending', 'processing', 'completed', 'failed') DEFAULT 'pending',
    chunk_count INT DEFAULT 0,
    error_message TEXT,
    processed_at TIMESTAMP NULL,
    processing_time_seconds INT,
    FOREIGN KEY (material_id) REFERENCES course_materials(id) ON DELETE CASCADE,
    INDEX idx_status (processing_status)
);
