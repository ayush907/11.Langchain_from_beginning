from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

model_id = ""  # put here the model you want to use

llm = HuggingFacePipeline.from_model_id(    # this will download the model locally on your pc
    model_id=model_id,
    task = "text-generation",
    pipeline_kwargs = dict(
        temperature = 0.5,
        max_new_tokens = 100,
        do_sample = True 
    )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Hello, how are you?")

print(result.content)