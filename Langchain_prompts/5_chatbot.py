from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(
    llm=llm
)

# Initialize chat history as an empty list
chat_history = []

while True:
    user_input = input("user : ")
    if user_input.lower() == "exit":
        break

    # Append user input with the correct role ('user')
    chat_history.append({"role": "user", "content": user_input})

    # Get the model's response
    result = model.invoke(chat_history)

    # Append assistant response with the correct role ('assistant')
    chat_history.append({"role": "assistant", "content": result.content})

    # Print the model's response
    print("Bot : ", result.content)

# Optionally print the full chat history
print(chat_history)
