import streamlit as st
import chromadb
# Initialize DB
client = chromadb.Client()
collection = client.get_or_create_collection(name="my_knowledge_base")

# Simple data
data = [
    {"id": "1", "text": "Python is a versatile programming language for AI.", "title": "Python AI"},
    {"id": "2", "text": "Vector databases store information as numbers for fast search.", "title": "Vector DBs"},
    {"id": "3", "text": "RAG helps AI answer questions using specific facts.", "title": "RAG Explained"}
]

# Store data (no embeddings, simple)
for item in data:
    collection.upsert(
        ids=[item["id"]],
        documents=[item["text"]],
        metadatas=[{"title": item["title"]}]
    )

# UI
st.title("🚀 AI Search Engine (Light Version)")
query = st.text_input("Enter your question:")

if query:
    results = collection.query(query_texts=[query], n_results=1)
    
    st.subheader("Top Result:")
    st.write(results["metadatas"][0][0]["title"])
    st.write(results["documents"][0][0])