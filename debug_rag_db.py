from database.db import fetch_all

print('Current database:')
print(fetch_all('SELECT DATABASE() AS db'))
print('\nTables matching material/chunk:')
print(fetch_all('SHOW TABLES LIKE %s', ('%material%',)))
print(fetch_all('SHOW TABLES LIKE %s', ('%chunk%',)))
print('\nMaterial processing status rows:')
print(fetch_all('SELECT * FROM material_processing_status LIMIT 10'))
print('\nChunk counts:')
print(fetch_all('SELECT COUNT(*) AS c FROM material_chunks'))
print(fetch_all('SELECT COUNT(*) AS c FROM chunk_embeddings'))
