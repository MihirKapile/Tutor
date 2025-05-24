# Multi-Agent Tutor API

This project delivers a multi-agent tutoring system powered by Google's Gemini models and the Agno framework, exposed via a Flask API. It features specialized agents for Math and Physics, alongside a general agent for query classification and fallback responses.

---

## Features

* **Multi-Agent Architecture**: Distinguishes between Math, Physics, and General queries for targeted assistance.
* **Tool Use**: The Math Agent can perform calculations, and the Physics Agent can look up constants.
* **API Access**: Interact with the tutor through a straightforward RESTful API endpoint.
* **Simple Web Interface**: A basic HTML/JavaScript frontend provides an easy way to chat with the tutor.
* **CORS Enabled**: Configured for seamless cross-origin requests from the frontend.

---

## Project Structure

tutor_api/
├── main.py                     # Flask application, orchestrator agent
├── agents/                     # Contains agent definitions
│   ├── __init__.py
│   ├── base_agent.py           # Base class for agents
│   ├── math_agent.py           # Math specialist agent
│   └── physics_agent.py        # Physics specialist agent
├── tools/                      # Contains tools agents can use
│   ├── __init__.py
│   ├── calculator.py           # Math calculation tool
│   └── constants_lookup.py     # Physics constants lookup tool
├── templates/                  # HTML templates for the frontend
│   └── index.html              # Main web interface
├── .env                        # Environment variables (e.g., API keys) - IGNORED BY GIT
└── requirements.txt            # Python dependencies

Setup and Installation
Clone the repository:
git clone <your-repository-url>
cd tutor_api
Create and activate a virtual environment:
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
Install dependencies:
pip install -r requirements.txt
If requirements.txt doesn't exist, generate it with:
pip freeze > requirements.txt
Configure Environment Variables
Create a file named .env in the root directory with the following content:
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
Important: Do not commit this file. It's already listed in .gitignore.
Running the Application
Run the Flask application using the built-in development server:
python main.py
The app will be available at: http://127.0.0.1:5000
API Endpoints
# 1. Ask the Tutor
URL: /ask
Method: POST
Content-Type: application/json
Request Body:
{
  "query": "Your question here, e.g., What is the speed of light?"
}
Success Response (200 OK):
{
  "response": "The tutor's answer to your question."
}
Error Response (400/500):
{
  "error": "Error message details."
}
Example curl command:
curl -X POST "http://127.0.0.1:5000/ask" \
     -H "Content-Type: application/json" \
     -d '{"query": "Calculate 25 * 10."}'
Frontend (Web Interface)
URL: /
Method: GET

Access http://127.0.0.1:5000/ in your web browser to use the chat interface. This uses JavaScript to interact with the /ask endpoint.
Environment Variables
# Ensure the following variable is set in your .env file:
GOOGLE_API_KEY: Your API key for accessing Google Gemini models.
