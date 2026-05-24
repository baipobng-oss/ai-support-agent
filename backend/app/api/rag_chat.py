from langchain.chains import RetrievalQA

def build_rag_chain(vector_store, llm):

    retriever = vector_store.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain