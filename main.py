from openai import OpenAI
import json
from tool_definitions import functions_metadata
from utils import call_function
from dotenv import load_dotenv
import os
load_dotenv()

# Load environment variables from .env file
# Ensure you have a .env file with OPENAI_API_KEY set
# Example .env file content:
# OPENAI_API_KEY=your_openai_api_key_here
# Initialize OpenAI client
# Ensure you have the OpenAI Python package installed
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def chat():
    user_message = input("You: ")
    messages = [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        functions=functions_metadata,
        function_call="auto",
    )

    message = response.choices[0].message

    if message.function_call:
        function_name = message.function_call.name
        arguments = json.loads(message.function_call.arguments)

        print(f"Calling backend function: {function_name} with {arguments}")

        result = call_function(function_name, arguments)

        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": user_message},
                message,
                {"role": "function", "name": function_name, "content": result},
            ]
        )

        assistant_message = second_response.choices[0].message.content
        print(f"Assistant: {assistant_message}")
    else:
        print(f"Assistant: {message.content}")

if __name__ == "__main__":
    while True:
        chat()