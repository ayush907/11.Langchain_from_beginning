from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables = ["topic"]
)

template2 = PromptTemplate(
    template = "write a 5 line summary on the following text.\n {text}",
    input_variables = ["text"]
)

prompt1 = template1.invoke({"topic": "black hole"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})

final_result = model.invoke(prompt2)
print(final_result.content)