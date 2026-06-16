import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

def add_vectors(vectors):
    vectors = np.array(vectors).astype("float32")
    index.add(vectors)

def search_vectors(query_vector, k=3):
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, k)

    return indices[0]