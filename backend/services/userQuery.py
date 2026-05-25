from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

from langchain_chroma import Chroma

import os
import json

from dotenv import load_dotenv

from services.prompt import DOCUMENTATION_PROMPT
from services.html_template import get_html

load_dotenv(override=True)

GOOGLE_API = os.getenv("GOOGLE_API_KEY")


def load_vector_store(chroma_dir: str):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
    )

    db = Chroma(
        persist_directory=chroma_dir,
        embedding_function=embeddings,
        collection_name="codebase"
    )

    return db

def generate_docs(db):

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash"
    )

    all_data = db.get()

    print("Total chunks:", len(all_data["documents"]))

    if not all_data["documents"]:
        print("No documents found in ChromaDB!")
        return None

    codebase = ""

    for document in all_data["documents"]:
        codebase += f"\n\n{'='*40}\n{document}\n"

    print("Sending to Gemini...")

    prompt = DOCUMENTATION_PROMPT.format(
        codebase=codebase
    )

    response = llm.invoke(prompt)

    raw = (
        response.content
        .strip()
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    data = json.loads(raw)

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

    html = get_html(data)

    return {
        "json_data": data,

        "files": {
            "DOCUMENTATION.md": md,
            "index.html": html
        }
    }


if __name__ == "__main__":

    import tempfile

    temp_dir = tempfile.mkdtemp(
        prefix="codebasedoc_"
    )

    chroma_dir = os.path.join(
        temp_dir,
        "chroma_db"
    )

    os.makedirs(chroma_dir, exist_ok=True)
    db = load_vector_store(chroma_dir)
    result = generate_docs(db)
    print(result)