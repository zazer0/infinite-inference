import litellm
import os

response = litellm.completion(
    model="openai/IlyaGusev/gemma-2-2b-it-abliterated",               # add `openai/` prefix to model so litellm knows to route to OpenAI
    #api_key="sk-1234",                  # api key to your openai compatible endpoint
    api_base="http://0.0.0.0:31892",     # set API Base of your Custom OpenAI Endpoint
    messages=[
                {
                    "role": "user",
                    "content": "Hey, how's it going?",
                }
    ],
)
print(response)
