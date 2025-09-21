# Name TBD

Solo-built AI coaching agent that turns a player's full year League match history into a shareable, data-driven end of year retrospectives. It pairs actionable coaching tips with fun, social-friendly highlights.\
Powered by AWS generative AI and the League API.

### Problem
Players want meaningful retrospectives that explain what changed over a season, where to improve, and fun shareables. Current stat sites provide numbers, but not personalized coaching, storytelling or creative shareables.

### Solution
An end-to-end agent that:
- Reads a player's full-year match history.
- Computes trends per champion, performance, vision, objectives.
- Uses AWS generative AI (Bedrock/ SageMaker) to produce:
    - Actionable insights: strenghts, growth areas, practice drills.
    - Engaging year-end narratives and social cards (helpful, but fun).
    - Visual progress charts and recommendations.
- Outputs should be downloadable/ sharable.

### Target Users
Casual to competitive League players who want to reflect, improve and share highlights at the end of the year.

### Core MVP features
- Upload or connect full-year match history (CSV/JSON)
- ETL pipline: Compute per-match metrics (KDA, CS/min, vision, objective participation)
- Season aggregates and simple time-series visualizations.
- LLM-generated one-paragraph recap and top 3 actionable tips (via Bedrock or SageMaker)
- Downloadable social card (PNG)
- Stable public demo link and public GitHub repo with license

### High-impact extras
- Roast and Coach mode outputs
- Hidden Gem Detector: Explains why an underrated champion or playstyle suits the player
- Social comparison percentile vs. friends
- Highlight match selector (best/worst/most improved)
- Small analytics dashboard (winrate trend, elo curve, champ heatmap)

### Technical Stack
- Frontend: React + Tailwind, hosted on S3/CloudFront or Amplify.
- API: API Gateway → AWS Lambda (Node/Python).
- Storage: S3 for raw & images; DynamoDB for summaries/cache.
- Analytics: Lambda or SageMaker Processing (Pandas).
- Generative AI: Amazon Bedrock (preferred) or SageMaker-hosted small model.
- Card generation: HTML → PNG via headless Chromium in Lambda or Fargate.
- Infra as Code: CDK/CloudFormation (simple templates).
