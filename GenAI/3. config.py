import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not set in environment")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="what is array?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=5000),
        system_instruction="You are a helpful assistant that provides concise answers to questions about current world leaders only. If any question is asked about a world leader then answer it otherwise say 'I can only answer questions about current world leaders like this , you can say anything else to me and I will not be able to answer it.'"
    )
)
print(response.text)
