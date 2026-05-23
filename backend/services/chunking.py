from services.parser_service import parsing_files

def devide_in_chunks(files):

    chunks = []
    chunk_id = 0
    for file in files:
  
        chunk = {
            "chunk_id": chunk_id,
            "file_type": file['file_type'],
            "file_name": file["file_name"],
            "path": file["path"],
            "content": file["file_content"]
        }

        chunks.append(chunk)
        chunk_id +=1

    return chunks