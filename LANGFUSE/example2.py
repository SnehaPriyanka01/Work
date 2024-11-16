import os
from ollama import Client  # Corrected the client initialization

# Set environment variables for LangFuse
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-753b3321-71c9-467a-8d65-e74be6bdf584"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-250688e6-69ba-4c70-80e1-bd0f3daa1df1"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"  # EU region

# Initialize the Ollama client with the base URL using the 'host' argument
client = Client(host='https://ollama.dealwallet.com')  # Use the Dealwallet endpoint

# Create a chat completion request using Ollama
response = client.chat( 
    model="llama3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who was the first person to step on the moon?"},
        {"role": "assistant", "content": "Neil Armstrong was the first person to step on the moon on July 20, 1969, during the Apollo 11 mission."},
        {"role": "user", "content": "What were his first words when he stepped on the moon?"}
    ]
)

# Access the assistant's response from the 'message' key
print(response['message']['content'])
