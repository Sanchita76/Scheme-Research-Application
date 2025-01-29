import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Print the API key
print(f"Retrieved API Key: {api_key}")
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")

try:
    models = client.models.list()
    print("API Key is working! Available models:")
    for model in models.data:
        print(model.id)
except Exception as e:
    print(f"Error: {e}")

