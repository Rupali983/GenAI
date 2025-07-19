import streamlit as st
from rag_chain import answer_question

st.title("💬 GenAI RAG Chatbot")
question = st.text_input("Ask a question about the database")

if question:
    response = answer_question(question)
    st.write(response)
