from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from chatbot.config import api_key, LLM_BASE_URL, MODEL
 

def chatmodel(docs,query):
    llm = ChatOpenAI(
        base_url=LLM_BASE_URL,
        openai_api_key=api_key,
        model=MODEL,
    )

    retrieved_context = "\n\n".join([doc.page_content for doc in docs])

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ( "system", "You are an assistant for question-answering tasks.Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.", ),
            ("human", "Context:\n{context}\n\nQuestion:\n{query}")
        ]
    )
    prompt=prompt_template.invoke({"context":retrieved_context,"query":query})
    response=llm.invoke(prompt)
    return response.content