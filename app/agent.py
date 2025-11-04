from app.retrieval import fetch_papers_for_query
from app.embedding_client import get_embedding
from app.utils import build_faiss_index, load_faiss, search_faiss
from app.llama3_client import  query_llama3
from app.utils import search_faiss
import numpy as np

def answer_biomedical_query(question, context_texts):
    # Build the prompt
    context = "\n\n".join(context_texts)
    prompt = f"""
You are a biomedical research assistant.
Using the context below, answer the following question concisely with citations.

Question: {question}

Context:
{context}

Answer:
"""
    response = query_llama3(prompt)
    return response

def answer_query(question):
    # 1. Get PubMed live papers
    papers = fetch_papers_for_query(question, max_results=20)
    if not papers:
        return {"answer": "No papers found. Try rephrasing.", "papers": []}


    # 2. Embed them
    embeddings = []
    for p in papers:
        embeddings.append(get_embedding(p["abstract"]))

    # 3. Build temp FAISS index
    build_faiss_index(embeddings, papers, index_path="data/faiss.index")
    index, metadata = load_faiss("data/faiss.index")
    q_emb = get_embedding(question)
    ids, dists = search_faiss(index, q_emb, topk=5)
    retrieved = [metadata[i] for i in ids]

    # 4. Call Llama-3
    prompt = query_llama3(question, retrieved)
    answer = query_llama3(prompt)

    # 5. Simple "confidence" check: if answer contains "insufficient" or short, refine
    if "insufficient" in answer.lower() or len(answer.split()) < 20:
        # refine query automatically
        refined = question + " review OR meta-analysis"
        more_papers = fetch_papers_for_query(refined, max_results=20)
        # (repeat embed+retrieve)
        # For speed, could append new papers to metadata and rerun retrieval
        return {"answer": answer + "\n\nAgent performed a refinement: " + refined,
                "papers": retrieved}
    return {"answer": answer, "papers": retrieved}
