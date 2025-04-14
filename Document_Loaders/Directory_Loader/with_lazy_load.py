from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Document_Loaders/Directory_Loader/sample_folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader 
)


# lazy_load() function returns a generator which manages the memory effeciently
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)