from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

SYSTEM_PROMPT = """
You are an AI customer support agent.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}")
])

chain = prompt | llm

def support_agent(message: str):

    result = chain.invoke({
        "input": message
    })

    return result.content