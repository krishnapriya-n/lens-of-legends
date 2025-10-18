import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

BASE_URL = "https://asia.api.riotgames.com/lol"

def get_puuid(summoner_name):
    """Get PUUID (unique player ID) from Summoner name"""
    url = f"{BASE_URL}/summoner/v4/summoners/by-name/{summoner_name}"
    res = requests.get(url, headers={"X-Riot-Token": API_KEY})
    return res.json().get("puuid")

def get_matches(puuid, count=20):
    """Get recent match IDs"""
    url = f"{BASE_URL}/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
    res = requests.get(url, headers={"X-Riot-Token": API_KEY})
    return res.json()

def get_match_details(match_id):
    """Get full match data"""
    url = f"{BASE_URL}/match/v5/matches/{match_id}"
    res = requests.get(url, headers={"X-Riot-Token": API_KEY})
    return res.json()
