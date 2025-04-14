from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path=r"C:\Users\dheka\Downloads\Ayush_Resume.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = " "
)

result = splitter.split_documents(docs)

print(f"length of the resultant splitted list is {len(result)}")
print(type(result[0]))

print(result[5].page_content)
print(result[5].metadata)