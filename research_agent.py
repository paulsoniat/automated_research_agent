from tools.search_tool import google_search
import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def summarize_url(url: str) -> str:
    return f"Placeholder summary for: {url}"  # Real implementation could scrape text and summarize

def generate_report(topic: str) -> str:
    links = google_search(topic)
    summaries = [summarize_url(url) for url in links]
    
    prompt = f"Write a 1-page report on '{topic}' using these summaries:\n\n" + "\n\n".join(summaries)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
