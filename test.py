from openai import OpenAI
from Holiday_Management.config.settings import OPENAI_API_KEY, MODEL_NAME
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": "Hello! how are you?"}
    ]
)

print(response.choices[0].message.content)