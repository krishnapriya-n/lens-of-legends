import os
import sys

sys.path.append("backend")
import insights  # your existing insights module

# Constants
SUMMONER_NAME = "Faker"  # test summoner

# --- Mock functions to replace Riot API calls ---
def fetch_summoner(name):
    print(f"Mock fetch summoner: {name}")
    return {"name": name, "summonerLevel": 100, "puuid": "dummy-puuid"}

def fetch_recent_matches(puuid, count=5):
    print(f"Mock fetch {count} recent matches for {puuid}")
    return [f"match_{i}" for i in range(count)]

def generate_mock_insight(match_ids):
    # Replace with your insights module logic if needed
    return insights.generate_insights({"matches": match_ids})

def main():
    if os.getenv("RIOT_API_KEY"):
        print("✅ Riot API key loaded successfully!")
    else:
        print("❌ Riot API key NOT found!")
        sys.exit(1)

    summoner = fetch_summoner(SUMMONER_NAME)
    print(f"Fetched summoner: {summoner['name']} (Level {summoner['summonerLevel']})")

    matches = fetch_recent_matches(summoner["puuid"])
    print(f"Recent {len(matches)} match IDs: {matches}")

    insight = generate_mock_insight(matches)
    print(f"Mock insight: {insight}")

if __name__ == "__main__":
    main()
