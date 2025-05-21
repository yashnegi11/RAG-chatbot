import os
import pprint
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_files(filenames):

    all_text=[]
    for filename in filenames:
        pdf_path = os.path.join('pdfs', filename)

        if not os.path.exists(pdf_path):
            print(f" File not found. {pdf_path}")
        else:
            print(f" File found. {filename}")

            loader = PyPDFLoader(pdf_path)
            pages = loader.load()
            
            for page in pages:
                all_text.append(page.page_content)
            # pprint.pp(pages[0].metadata)
    return all_text

def split_texts(all_text):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks=[]       
    for text in all_text:
        chunks = text_splitter.split_text(text)
        all_chunks.extend(chunks)
    # print(all_chunks[0])
    return all_chunks
