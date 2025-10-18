def generate_insights(data):
    """
    Generate sample insights from Riot match data.
    Later, you can connect this to AWS AI models or Bedrock.
    """
    if not data:
        return {"error": "No data provided"}

    name = data.get("summonerName", "Unknown Player")
    matches = data.get("matches", [])
    match_count = len(matches)

    return {
        "summary": f"{name} played {match_count} recent matches.",
        "tip": "Try to maintain a consistent KDA across matches to improve rank."
    }
