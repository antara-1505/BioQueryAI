import faiss
import numpy as np
import pickle

def build_faiss_index(embeddings, metadata_list, index_path="data/faiss.index", dim=None):
    # embeddings: list[list[float]]
    emb = np.array(embeddings).astype("float32")
    dim = emb.shape[1] if dim is None else dim
    index = faiss.IndexFlatL2(dim)
    index.add(emb)
    faiss.write_index(index, index_path)
    # save metadata
    with open(index_path + ".meta", "wb") as f:
        pickle.dump(metadata_list, f)

def load_faiss(index_path="data/faiss.index"):
    index = faiss.read_index(index_path)
    with open(index_path + ".meta", "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

def search_faiss(index, query_embedding, topk=5):
    D, I = index.search(np.array([query_embedding]).astype("float32"), topk)
    return I[0], D[0]
