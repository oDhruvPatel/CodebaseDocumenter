import google.genai as genai
import chromadb
import os
from dotenv import load_dotenv

load_dotenv(override=True)
GOOGLE_API = os.getenv("GOOGLE_API_KEY")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "chroma_db"))

client = genai.Client(api_key=GOOGLE_API)


def clear_embeddings():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    try:
        collection = chroma_client.get_collection("codebase")
        existing = collection.get()
        if existing["ids"]:
            collection.delete(ids=existing["ids"])
            print(f"Cleared {len(existing['ids'])} old chunks!")
        else:
            print("No old chunks to clear!")
    except Exception as e:
        print(f"Collection doesn't exist yet: {e}")

def embeddings(chunks):

    clear_embeddings()

    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name="codebase")

    for chunk in chunks:
        content_to_embed = f"Chunk_Id: {[chunk['chunk_id']]} File_name: {chunk['file_name']} File_type: {chunk['file_type']} Path: {chunk['path']} File_content: {chunk['content']}"
        
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=content_to_embed,
        )

        embedding = result.embeddings[0].values

        collection.add(
            ids=[str(chunk['chunk_id'])],
            embeddings=[embedding],
            documents=[content_to_embed],
            metadatas=[{
                "file_name": chunk['file_name'],
                "path": chunk['path'],
                "file_type": chunk['file_type'],
            }]
        )
        print(f"Saved chunk {chunk['chunk_id']} to: {CHROMA_PATH}")

    return collection