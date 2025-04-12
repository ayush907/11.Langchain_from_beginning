from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

load_dotenv()

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
    ("system", "you are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])


chat_history = list()
# load chat history
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())


prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "where is my refund"
})

print(prompt)
