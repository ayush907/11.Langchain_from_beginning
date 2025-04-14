from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
LangChain ek open-source framework hai jo developers ko LLM-based applications banane mein madad karta
hai. Yeh framework components ko modular banata hai jaise prompt templates, memory integration, tools
aur chains — jisse aap complex workflows easily build kar sakte ho.

Dusri taraf, jab aapko large texts ko manage karna ho — chahe embeddings ke liye ho ya retrieval-based
QA ke liye — tab text splitting bahut important hota hai. LangChain ka `RecursiveCharacterTextSplitter`
smartly paragraphs ya logical breaks ke basis pe text ko chunks mein divide karta hai. Isse na sirf
context preserve hota hai, balki performance bhi optimize hoti hai. Yeh string ab aapke splitter tests
ke liye ready hai!
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(result)
print(len(result))

for i in range(len(result)):
    print(result[i])
    print("*" * 40)
