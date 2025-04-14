from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

loader = TextLoader("Document_Loaders\Text_Loader\poem.txt", encoding="utf-8")

docs = loader.load()

prompt = PromptTemplate(
    template="write a summary for the following poem \n {poem}",
    input_variables=["poem"]
)

chain = prompt | model | parser

result = chain.invoke({"poem" : docs[0].page_content})

print(result)
