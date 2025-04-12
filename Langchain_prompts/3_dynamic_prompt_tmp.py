from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()


load_dotenv()

repo_id1 = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id1,
    task="text-generation", 
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input = st.selectbox("Select research paper name", ["Select...", "Attention is all you need", "BERT: pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GAN on image Synthesis"])

style_input = st.selectbox("Select Explaination Style", ["Beginner-Friendly", "Technical", "Code-oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explaination)"])

# template = PromptTemplate(
#     template="""  
# Please summarize the research paper titled "{paper_input}" with the following specifications:  

# Explanation Style: {style_input}  
# Explanation Length: {length_input}  

# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=["paper_input", "style_input", "length_input"],
# validate_template=True
# )

template = load_prompt("template.json")

prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    }
)
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    