from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id = repo_id,
    task = "text-generation", 
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

template = PromptTemplate(
    template = "Generate 5 interesting facts about the {topic}",
    input_variables = ["topic"]
)

chain = template | model | parser

result = chain.invoke({"topic" : "cricket"})

print(result)

chain.get_graph().print_ascii()