from flask import Flask
app = Flask(__name__)

# import your other modules here
import riot_api
import insights
import aws_ai

@app.route('/')
def home():
    return "Lens of Legends Backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
