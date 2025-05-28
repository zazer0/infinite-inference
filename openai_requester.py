import openai
import sys

PORT=sys.argv[1]


client = openai.Client(base_url=f"http://127.0.0.1:{PORT}/v1", api_key="none")

response = client.chat.completions.create(
    model="openai/IlyaGusev/gemma-2-2b-it-abliterated",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print(f"GOT Response: {response}")
