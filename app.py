import streamlit as st
import os
from chatbot.load_pdf import load_files, split_texts
from chatbot.embedding import embedding_and_storing_vectors
from chatbot.llm import chatmodel


# filenames = ['ArtificialIntelligenceWhatisit-RiturajMahato.pdf','Intern Assignment.pdf']


st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title('RAG- powered CHATBOT')

uploaded_files = st.file_uploader(
    "Upload your documents (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if uploaded_files:
    with st.spinner("Processing documents..."):
        filenames = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join("pdfs", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            filenames.append(uploaded_file.name)
        
        all_text_returned=load_files(filenames)
        all_chunks_returned=split_texts(all_text_returned)
        vectorstore=embedding_and_storing_vectors(all_chunks_returned)
        retriever = vectorstore.as_retriever(search_kwargs={'k': 3})

        st.success("Documents processed. You can start chatting now!")

        # Chat input
        query = st.chat_input("Ask something about your documents:")
        if query:
            st.session_state.messages.append({"role": "user", "content": query})

            with st.spinner("Thinking..."):
                docs = retriever.invoke(query)
                answer = chatmodel(docs, query)
                st.session_state.messages.append({"role": "assistant", "content": answer})

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


    