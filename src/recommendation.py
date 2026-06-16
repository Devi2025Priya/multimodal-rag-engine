import pandas as pd

from src.embeddings import get_text_embedding
from src.vector_store import add_vectors
from src.vector_store import search_vectors

df = pd.read_csv("data/products.csv")

embeddings = []

for description in df["description"]:
    embedding = get_text_embedding(description)
    embeddings.append(embedding)

add_vectors(embeddings)


def recommend(query):

    query_embedding = get_text_embedding(query)

    indices = search_vectors(query_embedding)

    recommendations = []

    for idx in indices:
        recommendations.append(df.iloc[idx]["name"])

    return recommendations