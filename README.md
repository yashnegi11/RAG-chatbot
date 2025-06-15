# 📚 RAG-Powered PDF Chatbot

An interactive **Streamlit application** that allows users to upload multiple documents (PDF, DOCX, TXT) and **chat with their contents** using **Retrieval Augmented Generation (RAG)**.

---

## 🚀 Features

- Upload multiple documents
- Intelligent chunking and vector embedding using Hugging Face
- Semantic search with FAISS vector store
- Answer user queries with context-aware responses from the documents
- Built with **LangChain**, **Streamlit**, and **OpenRouter/LLM API**

---

## 📝 Architecture Diagram

![Image](<rag implementation diagram.png>)

---

## 🌐 Live Demo

Try the app here:  
👉 [Launch on Streamlit](https://rag-chatbot-p4h8isbncpu4ugctpxprvo.streamlit.app/)

---

## 🎥 Video Walkthrough

Watch a short demo of how TalentScout works:  
▶️ [Demo Video on Google Drive](https://drive.google.com/file/d/1_IRuWCn5AzvsihzNxX4_k-UyneEYl52a/view?usp=sharing)

---

## 🧰 Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
- [OpenRouter.ai](https://openrouter.ai/) (LLM API)

---

## 📂 Project Structure

```
chatbot/
├── app.py                     # Streamlit UI
├── chatbot/
│   ├── __init__.py
│   ├── load_pdf.py            # PDF loading and splitting
│   ├── embedding.py           # Embedding and FAISS index 
│   └── llm.py                 # Prompt and LLM response
├── faiss_index/               # Vector DB (auto-created)
├── pdfs/                      # Uploaded PDFs
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yashnegi11/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # or source venv/bin/activate on MacOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 License

MIT License

---

## 🙋‍♂️ Author

Made with ❤️ by [Yash Pal Singh Negi]
(https://github.com/yashnegi11)
