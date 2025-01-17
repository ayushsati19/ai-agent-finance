import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv('.env', override=True)

# Check if the API key is loaded correctly
api_key = os.getenv('API_KEY')  # Change to 'groq_api_key' if using lowercase

if api_key:
    print("PHI_API_KEY is loaded:", api_key)
else:
    print("API_KEY not found. Please set the key in the .env file.")
