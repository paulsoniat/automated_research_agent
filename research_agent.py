import os
from dotenv import load_dotenv
from openai import OpenAI
from tools.search_tool import google_search

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_url(url: str) -> str:
    return f"Summary for: {url}"

def generate_report(topic: str) -> str:
    links = google_search(topic)
    summaries = [summarize_url(url) for url in links]

    prompt = f"Write a 1-page report on '{topic}' using these summaries:\n\n" + "\n\n".join(summaries)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
