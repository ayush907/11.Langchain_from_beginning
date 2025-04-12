from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
import os

load_dotenv()


model = ChatOpenAI("gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

# schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "title": "Key Themes",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "write down all the key themes discussed in the review in a list"
        },
        "summary": {
            "title": "Summary",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "title": "Sentiment",
            "type": "string",
            "enum": [
                "pos",
                "neg"
            ],
            "description": "return sentiment of the review either negative positive or neutral"
        },
        "pros": {
            "title": "Pros",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "write down all the pros inside a list"
        },
        "cons": {
            "title": "Cons",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "write down all the cons inside a list"
        },
        "name": {
            "title": "Name",
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "write down the name of the reviewer"
        }
    },
    "required": [
        "key_themes",
        "summary",
        "sentiment"
    ]
}


structured_model = model.with_structured_output(json_schema)


result = structured_model.invoke('''the herdware is great but the software feels bloated. there are too many pre-installed 
                      applictions thet I can't remove. Also, the UI looks outdated compared to other brands.
                      hoping for a software update to fix this''')

print(result)


