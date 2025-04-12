from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import os

# Load environment variables
load_dotenv()

# Correct model initialization with "model" keyword argument
model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

# Define schema for structured output
class Review(TypedDict):
    key_themes: Annotated[list[str], "write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "a brief summary of the review"]
    sentiment: Annotated[str, "return sentiment of the review either negative, positive, or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]
    name: Annotated[Optional[str], "write the name of the reviewer"]

# Attach structured output to model
structured_model = model.with_structured_output(Review)

# Review text
review_text = '''the hardware is great but the software feels bloated. there are too many pre-installed 
applications that I can't remove. Also, the UI looks outdated compared to other brands.
hoping for a software update to fix this'''

# Invoke the model with the review text
result = structured_model.invoke(review_text)

# Print the result which will be structured as defined in `Review`
print(result)
