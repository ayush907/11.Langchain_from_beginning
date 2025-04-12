import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Chat history (store previous messages)
chat_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]

# Function to send new messages and maintain chat history
def send_message(content):
    chat_history.append({"role": "user", "content": content})
    
    try:
        # Call the API with updated chat history
        response = client.chat.completions.create(
            messages=chat_history,
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        
        # Get assistant's response
        assistant_response = response.choices[0].message.content
        
        # Add assistant's response to the chat history
        chat_history.append({"role": "assistant", "content": assistant_response})
        
        # Return assistant's response
        return assistant_response
    
    except Exception as e:
        # Error handling in case of API failure or incorrect input
        return f"Error: {str(e)}"

# Example usage: Send a new message and get the response
while True:
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Assistant: Goodbye!")
        break
    
    content = user_input
    response = send_message(content)
    print("Assistant:", response)
