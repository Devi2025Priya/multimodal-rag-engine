import streamlit as st
from src.recommendation import recommend

st.title("Multimodal RAG Recommendation Engine")

query = st.text_input("Enter Product Description")

if st.button("Recommend"):

    recommendations = recommend(query)

    st.subheader("Recommended Products")

    for item in recommendations:
        st.write(item)