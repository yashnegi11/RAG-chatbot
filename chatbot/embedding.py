import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def embedding_and_storing_vectors(all_chunks):

    # Hugging Face Embedding Model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    # FAISS vectorestore
    # if os.path.exists("faiss_index/index.faiss"):
    #     print("loading exitiing FAISS index")
    #     vectorstores = FAISS.load_local("faiss_index",  embeddings, allow_dangerous_deserialization=True)
    # else :
    #     print("creating new FAISS index:")
    #     vectorstores = FAISS.from_texts(all_chunks, embedding=embeddings)
    #     vectorstores.save_local("faiss_index")

    vectorstores = FAISS.from_texts(all_chunks, embedding=embeddings)
    return vectorstores
