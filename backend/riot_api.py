import os
import requests

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

if not RIOT_API_KEY:
    raise ValueError("RIOT_API_KEY not found — make sure it’s set as a GitHub Secret.")

BASE_URL = "https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

def get_summoner_info(summoner_name):
    """Fetch basic summoner info using Riot API"""
    url = f"{BASE_URL}{summoner_name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data: {response.status_code}", "details": response.text}
