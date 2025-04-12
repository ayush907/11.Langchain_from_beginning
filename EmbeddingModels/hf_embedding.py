from langchain_huggingface import HuggingFaceEmbeddings

model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=model_name)

text = "India ki capital kya hai?"

embedding = embeddings.embed_query(text)

print(embedding)
print(type(embedding))
print(len(embedding))