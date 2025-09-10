import requests
from bs4 import BeautifulSoup
from typing import Dict
import json

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