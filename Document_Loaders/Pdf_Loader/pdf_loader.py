from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Document_loaders/Pdf_Loader/ten_page_sample.pdf")

docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)