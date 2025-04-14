from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path="Document_Loaders/Directory_Loader/sample_folder",
    glob="*.txt",
    loader_cls=TextLoader
)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)