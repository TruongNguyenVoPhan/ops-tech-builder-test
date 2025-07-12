from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

text_input = """
Sarah and Michael traveled to Bangkok on December 15, 2023 for a conference. They flew from New York and will return on December 22nd. During their stay, they plan to visit the Grand Palace and meet with Professor Chen at Chulalongkorn University.
They also intend to try local cuisine and explore the markets.
"""

prompt = "Extract names, dates, and locations from the following paragraph"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"{prompt}\n\n{text_input}"}
    ],
    temperature=0.5,
    max_tokens=150
)

print("GPT Response:")
print(response.choices[0].message.content.strip())