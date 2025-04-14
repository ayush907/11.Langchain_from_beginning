from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

markdown_text = """
# 🧠 AI Basics

Artificial Intelligence (AI) allows machines to mimic human intelligence like learning and decision-making.

---

## 🔍 What is AI?

AI refers to machines programmed to simulate human-like capabilities such as problem-solving and pattern recognition.

---

## 📚 Types of AI

- **Narrow AI**: Task-specific (e.g., Siri)  
- **General AI**: Human-level intelligence  
- **Super AI**: Beyond human intelligence

---

## ⚙️ Core Areas

### 🤖 Machine Learning

Enables systems to learn from data.

### 🧠 Deep Learning

Uses neural networks to process complex data.

---

## 🧪 Challenges

- Data bias  
- Privacy concerns  
- Ethical dilemmas

> ⚠️ Ensure responsible AI development.

---

## ✅ Summary

AI is evolving fast and needs to be developed responsibly to benefit society.

"""



splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size = 170,
    chunk_overlap = 0
)

result = splitter.split_text(markdown_text)

print(result)

for chunk in result:
    print(chunk)
    print("-" * 30)

