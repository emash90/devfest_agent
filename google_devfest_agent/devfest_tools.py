import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import json
import re
from google.adk.tools import google_search

"""
define the 4 tools to get the data on devfests


scrape_devfest_event_details
search_for_devfest_images(location)
generate_social_media_post(event_name, summary)

"""

def scrape_devfest_event_details(url: str) -> Dict:
    """
    Scrapes DevFest event info for events on November 1st from a GDG page.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Basic info
        title = soup.select_one("h1")
        when = soup.find(string=lambda s: "Nov 1" in s) or ""
        where = soup.find(string=lambda s: "Where" in s)
        speakers = [s.get_text(strip=True) for s in soup.select("## Speakers ~ div > div")]

        return {
            "title": title.get_text(strip=True) if title else "",
            "when": when.strip(),
            "where": where.strip() if where else "",
            "speakers": speakers or []
        }

    except Exception as e:
        return {"error": str(e)}

def extract_urls_from_text(text: str) -> List[str]:
    """Helper: extract all URLs from search output."""
    return re.findall(r"(https?://[^\s]+)", text)


def search_for_devfest_images(city: str) -> Dict:
    """
    Use Google Search tool to find DevFest images for a given city.
    """
    try:
        query = f"DevFest {city} site:images.google.com"
        search_output = google_search(query)

        urls = extract_urls_from_text(str(search_output))
        image_urls = [u for u in urls if any(ext in u.lower() for ext in [".jpg", ".jpeg", ".png"])]

        return {"city": city, "images": image_urls[:5]}  # return top 5

    except Exception as e:
        return {"error": str(e)}
    

def generate_social_media_post(event_name: str, summary: str) -> str:
    """Generate a social media post for a DevFest event."""
    try:
        return f"🚀 Exciting times at {event_name}! {summary} 🎉 #DevFest #AI #GoogleDevelopers"
    except Exception as e:
        return f"Error generating post: {str(e)}"