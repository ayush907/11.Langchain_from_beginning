from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
)

model = ChatHuggingFace(
    llm=llm
)

chat_template = ChatPromptTemplate([
    ("system", "you are a helpful {domain} expert"),
    ("human", "explain is simple terms  {topic}")
])


prompt = chat_template.invoke({"domain" : "cricket", "topic" : "dusra"})

# print(prompt)

result = model.invoke(prompt)

print(result.content)

