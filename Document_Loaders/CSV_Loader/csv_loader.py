from langchain_community.document_loaders import CSVLoader


path = r"C:\Users\dheka\Downloads\churn_dataset\Churn_Modelling.csv"

loader = CSVLoader(
    file_path = path
)

# in CSVLoader each row in the dataframe loads as a single documant

docs = loader.load()

print(f"the length of the document is {len(docs)}")

# print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)