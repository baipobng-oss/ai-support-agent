import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI support agent."
    ),
    (
        "human",
        "{input}"
    )
])

chain = prompt | llm

def support_agent(message: str):

    result = chain.invoke({
        "input": message
    })

    return result.content