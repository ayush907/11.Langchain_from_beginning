from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import os

load_dotenv()


model = ChatOpenAI("gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

# schema
class Review (TypedDict):
    key_themes: Annotated[list[str], "write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "a brief summary of the review"]
    sentiment: Annotated[str, "return sentiment of the review either negative positive or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]
    name: Annotated[Optional[list[str]], "write the name of the reviewer"]

structured_model = model.with_structured_output(Review)


result = structured_model.invoke('''the herdware is great but the software feels bloated. there are too many pre-installed 
                      applictions thet I can't remove. Also, the UI looks outdated compared to other brands.
                      hoping for a software update to fix this''')

print(result)

