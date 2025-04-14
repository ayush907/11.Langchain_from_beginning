from langchain_community.document_loaders import TextLoader

loader = TextLoader("Document_Loaders\Text_Loader\poem.txt", encoding="utf-8")

docs = loader.load()

# print(docs)      # list of docuents
# print(type(docs))
# print(len(docs))
# print(docs[0])   # it is an document object (<class 'langchain_core.documents.base.Document'>)
print(docs[0].page_content)
print(docs[0].metadata)