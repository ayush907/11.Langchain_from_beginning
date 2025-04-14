from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Document_Loaders/Directory_Loader/sample_folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader 
)

docs = loader.load()

print(len(docs))

print(docs[20].page_content)
print(docs[20].metadata)