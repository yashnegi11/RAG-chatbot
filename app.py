import streamlit as st
import os
from chatbot.load_pdf import load_files, split_texts
from chatbot.embedding import embedding_and_storing_vectors
from chatbot.llm import chatmodel
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title('🤖 RAG-powered Chatbot')

if "api_validated" not in st.session_state:
    st.session_state.api_validated = False
if "retriever" not in st.session_state:
    st.session_state.retriever = None

if not st.session_state.api_validated:
    api_key_input = st.text_input("🔑 Enter your OpenRouter API Key:", type="password")
    if api_key_input:
        try:
            llm = ChatOpenAI(
                base_url="https://openrouter.ai/api/v1",
                openai_api_key=api_key_input,
                model="deepseek/deepseek-r1:free",
            )
            llm.invoke("Hello")  
            st.session_state.api_validated = True
            st.session_state.api_key = api_key_input
            st.success("✅ API key is valid. You can now upload documents.")
        except Exception:
            st.error("❌ Invalid API key. Please try again.")
            st.stop()
else:
    st.info("🔐 API key is already set and valid.")

if st.session_state.api_validated and st.session_state.retriever is None:
    uploaded_files = st.file_uploader("📄 Upload your documents (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    if uploaded_files:
        with st.spinner("📚 Processing documents..."):
            filenames = []
            for uploaded_file in uploaded_files:
                os.makedirs("pdfs", exist_ok=True)
                file_path = os.path.join("pdfs", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                filenames.append(uploaded_file.name)

            all_text_returned = load_files(filenames)
            all_chunks_returned = split_texts(all_text_returned)
            vectorstore = embedding_and_storing_vectors(all_chunks_returned)
            retriever = vectorstore.as_retriever(search_kwargs={'k': 3})
            st.session_state.retriever = retriever
            st.success("✅ Documents processed. You can now start chatting.")

if st.session_state.retriever:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    query = st.chat_input("💬 Ask something about your documents:")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.spinner("🤖 Thinking..."):
            docs = st.session_state.retriever.invoke(query)
            answer = chatmodel(docs, query, st.session_state.api_key)
            st.session_state.messages.append({"role": "assistant", "content": answer})

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
