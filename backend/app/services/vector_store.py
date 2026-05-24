from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore

embeddings = OpenAIEmbeddings()

def create_vector_store(chunks, client):

    vector_store = SupabaseVectorStore.from_documents(
        chunks,
        embeddings,
        client=client,
        table_name="documents"
    )

    return vector_store