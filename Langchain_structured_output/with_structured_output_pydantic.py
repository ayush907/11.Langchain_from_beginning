from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
import os

load_dotenv()


model = ChatOpenAI("gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

# schema
class Review (BaseModel):
    key_themes: list[str] = Field(description="write down all the key themes discussed in the review in a list")
    summary: list[str] = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="return sentiment of the review either negative positive or neutral")
    pros: Optional[list[str]] = Field(description="write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description="write down all the cons inside a list")
    name: Optional[list[str]] = Field(description="write dwon the name of the reviewer")

structured_model = model.with_structured_output(Review)


result = structured_model.invoke('''the herdware is great but the software feels bloated. there are too many pre-installed 
                      applictions thet I can't remove. Also, the UI looks outdated compared to other brands.
                      hoping for a software update to fix this''')

print(result)
print(result.name)

