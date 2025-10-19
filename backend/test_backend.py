import os
import sys
import requests

sys.path.append("backend")
import insights  # your existing insights module

# Constants
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
SUMMONER_NAME = "Faker"  # test summoner
REGION = "na1"           # adjust as needed

def fetch_summoner(name):
    url = f"https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"❌ Failed to fetch summoner: {r.status_code} {r.text}")
        sys.exit(1)

def fetch_recent_matches(puuid, count=5):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"❌ Failed to fetch matches: {r.status_code} {r.text}")
        sys.exit(1)

def generate_mock_insight(match_ids):
    # Use your insights module for real logic; for now, a placeholder
    return insights.generate_insights({"matches": match_ids})

def main():
    print("✅ Riot API key loaded successfully!")
    summoner = fetch_summoner(SUMMONER_NAME)
    print(f"Fetched summoner: {summoner['name']} (Level {summoner['summonerLevel']})")

    matches = fetch_recent_matches(summoner["puuid"])
    print(f"Recent {len(matches)} match IDs: {matches}")

    insight = generate_mock_insight(matches)
    print(f"Mock insight: {insight}")

if __name__ == "__main__":
    main()
