import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from agno.agent import Agent
from agno.models.google import Gemini
import asyncio
from flask_cors import CORS
load_dotenv()

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it in your .env file.")

from agents import MathAgent, PhysicsAgent

class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.classifier_agent = Agent(
            model=Gemini(id="gemini-2.0-flash"),
            instructions=[
                "Your sole purpose is to classify user queries into one of these categories: 'Math', 'Physics', or 'General'.",
                "Respond with only the category name, e.g., 'Math', 'Physics', 'General'.",
                "Do not add any other text."
            ]
        )
        self.general_agent = Agent(
            model=Gemini(id="gemini-2.0-flash"),
            instructions=[
                "You are a general assistant. If a query is not about Math or Physics, offer to help within those subjects.",
                "Be polite and helpful."
            ]
        )

    async def classify_query(self, query: str) -> str:
        response = self.classifier_agent.run(f"Classify: {query}")
        return response.content.strip()

    async def process_query(self, query: str) -> str:
        category = await self.classify_query(query)
        print(f"Detected category: {category}")

        if category == 'Math':
            return await self.math_agent.handle_query(query)
        elif category == 'Physics':
            return await self.physics_agent.handle_query(query)
        elif category == 'General':
            general_response = await self.general_agent.run(f"You asked: '{query}'. I can answer questions about Math and Physics. How can I help you within those subjects?")
            return general_response.content
        else:
            return "I'm sorry, I couldn't determine the subject of your question. Please ask a question related to Math or Physics."

app = Flask(__name__, template_folder='templates')
CORS(app)

tutor_agent_instance = TutorAgent()

@app.route("/", methods=["GET"])
def index():
    """
    Serves the simple HTML frontend for interacting with the Tutor Agent.
    """
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_tutor():
    """
    API endpoint to send a question to the Tutor Agent and get a response.
    """
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = asyncio.run(tutor_agent_instance.process_query(user_query))
        return jsonify({"response": response})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == "__main__":
    print("Running Flask app. Visit http://127.0.0.1:5000")
    app.run(debug=True, port=5000)