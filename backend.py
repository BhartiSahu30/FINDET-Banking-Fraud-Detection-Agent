import requests
import json

# -----------------------------
# 1. Local LLM (Ollama اتصال)
# -----------------------------
def query_ollama(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]


# -----------------------------
# 2. Mock Database (Profiles)
# -----------------------------
profiles_db = {
    "101": {
        "name": "Bharti Sahu",
        "age": 21,
        "transactions": [1200, 4500, 300, 9800],
        "risk_score": 0.2
    },
    "102": {
        "name": "Rahul Verma",
        "age": 34,
        "transactions": [15000, 22000, 50000],
        "risk_score": 0.85
    }
}


# -----------------------------
# 3. API Logic (Tool Layer)
# -----------------------------
def fetch_user_profile(user_id):
    """Simulates API call to fetch user data"""
    return profiles_db.get(user_id, None)


# -----------------------------
# 4. Agent Logic (Brain)
# -----------------------------
def fraud_detection_agent(user_id):
    user_data = fetch_user_profile(user_id)

    if not user_data:
        return "User not found."

    # Prepare structured input for LLM
    prompt = f"""
    You are a fraud detection AI agent.

    Analyze the following user data and determine if there is suspicious activity.

    User Data:
    Name: {user_data['name']}
    Age: {user_data['age']}
    Transactions: {user_data['transactions']}
    Risk Score: {user_data['risk_score']}

    Give:
    1. Risk Level (Low, Medium, High)
    2. Reason
    3. Recommendation
    """

    response = query_ollama(prompt)
    return response


# -----------------------------
# 5. Entry Point (Test Run)
# -----------------------------
if __name__ == "__main__":
    user_id = "102"
    result = fraud_detection_agent(user_id)

    print("\n🧠 Agent Analysis:\n")
    print(result)