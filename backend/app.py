from flask import Flask, jsonify, request
from riot_api import get_summoner_info
from insights import generate_insights

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Lens of Legends Backend is running!"})

@app.route("/summoner/<string:summoner_name>")
def summoner(summoner_name):
    # Fetch summoner info from Riot API
    summoner = get_summoner_info(summoner_name)
    if "error" in summoner:
        return jsonify(summoner), 400

    # For now, simulate recent matches (replace with match-v5 API later)
    recent_matches = [{"matchId": f"match_{i}"} for i in range(5)]
    
    # Add puuid so insights can use it if needed
    summoner["matches"] = recent_matches

    # Generate insights
    insight = generate_insights(summoner)

    return jsonify({
        "summoner": summoner,
        "insights": insight
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
