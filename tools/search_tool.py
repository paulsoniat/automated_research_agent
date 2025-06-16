from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

def google_search(query: str, num_results=5):
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": num_results
    })
    results = search.get_dict()
    return [r["link"] for r in results.get("organic_results", [])]
