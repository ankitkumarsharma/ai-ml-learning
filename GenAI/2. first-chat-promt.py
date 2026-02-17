import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not set in environment")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Who is PM of India?"
)
print(response.text)
