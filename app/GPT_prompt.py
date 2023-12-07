import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def get_resp_gpt(user_input, api_key):
    if not api_key:
        raise ValueError("API key not found in environment variables")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I'm looking for song recommendations. Please recommend 10 songs for me, given the context to be: '{user_input}' Please provide the song titles first, followed by the artists' names, all together.",
        max_tokens=150,
        api_key=api_key,
    )

    return response.choices[0].text
