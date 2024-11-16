import os
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-753b3321-71c9-467a-8d65-e74be6bdf584"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-250688e6-69ba-4c70-80e1-bd0f3daa1df1"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com" # 🇪🇺 EU region
# os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region
from langfuse.openai import OpenAI
 
# Configure the OpenAI client to use http://localhost:11434/v1 as base url 
client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
 
response = client.chat.completions.create(
  model="llama3.1",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who was the first person to step on the moon?"},
    {"role": "assistant", "content": "Neil Armstrong was the first person to step on the moon on July 20, 1969, during the Apollo 11 mission."},
    {"role": "user", "content": "What were his first words when he stepped on the moon?"}
  ]
)
print(response.choices[0].message.content)
