from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
import os
import json
from services.prompt import DOCUMENTATION_PROMPT
from services.html_template import get_html
from dotenv import load_dotenv

load_dotenv(override=True)
GOOGLE_API = os.getenv("GOOGLE_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CHROMA_DIR = os.path.join(BASE_DIR, "..", "chroma_db")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
    )
    db = Chroma(
        persist_directory=CHROMA_DIR, 
        embedding_function=embeddings,
        collection_name="codebase"
    )
    return db


def save_markdown(data):
    md = f"# {data['project_name']}\n\n"
    for file in data['files']:
        md += f"## {file['name']}\n"
        md += f"{file['purpose']}\n\n"
        md += "**Functions:**\n"
        for f in file['functions']:
            md += f"- {f}\n"
        md += "\n**Dependencies:**\n"
        for d in file['dependencies']:
            md += f"- {d}\n"
        md += "\n---\n\n"

    with open(os.path.join(OUTPUT_DIR, "DOCUMENTATION.md"), "w", encoding="utf-8") as f:
        f.write(md)
    print("DOCUMENTATION.md saved!")


def save_html(data):
    html = get_html(data)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html saved!")


def generate_docs(db):
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
    all_data = db.get()
    print("Total chunks:", len(all_data["documents"]))

    if not all_data["documents"]:
        print("No documents found in ChromaDB!")
        return

    codebase = ""
    for document in all_data["documents"]:
        codebase += f"\n\n{'='*40}\n{document}\n"

    print("Sending to Gemini...")
    prompt = DOCUMENTATION_PROMPT.format(codebase=codebase)
    response = llm.invoke(prompt)

    raw = response.content.strip().replace("```json", "").replace("```", "").strip()
    data = json.loads(raw)

    save_markdown(data)
    save_html(data)

if __name__ == "__main__":
    db = load_vector_store()
    generate_docs(db)