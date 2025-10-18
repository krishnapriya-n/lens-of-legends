from flask import Flask, jsonify, request
from riot_api import get_summoner_info
from insights import generate_insights
from aws_ai import analyze_with_bedrock

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend running successfully!"})

@app.route("/summoner", methods=["GET"])
def summoner():
    summoner_name = request.args.get("name")
    if not summoner_name:
        return jsonify({"error": "Summoner name is required"}), 400

    data = get_summoner_info(summoner_name)
    return jsonify(data)

@app.route("/insights", methods=["POST"])
def insights():
    data = request.json
    insights = generate_insights(data)
    return jsonify(insights)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json.get("text", "")
    result = analyze_with_bedrock(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
