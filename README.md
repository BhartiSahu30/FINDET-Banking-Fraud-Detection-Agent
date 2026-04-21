# 🛡️ FINDET – Banking Fraud Detection Agent

An intelligent **AI-powered fraud detection system** that analyzes user transaction data and identifies suspicious activities using a **local LLM (Ollama - Llama 3.2)**.

---

## 🚀 Overview

FINDET is designed as an **Agentic AI System** that combines:

* 🧠 **LLM Reasoning (Brain)** – Decision-making using Llama 3.2
* 👁 **Tool Usage (Eyes)** – Fetching user financial data
* 🗂 **Mock Database** – Simulated banking profiles
* ⚙️ **Backend Logic** – Modular Python architecture

The agent evaluates transaction patterns and generates:

* Risk Level (Low / Medium / High)
* Explanation
* Actionable Recommendations

---

## 🧠 Architecture

```
User Input → Agent → Tool (Fetch Data) → LLM → Response
```

### Components:

* **Agent Layer** → Fraud detection logic
* **Tool Layer** → Data fetching functions
* **Database Layer** → Mock user profiles
* **LLM Layer** → Ollama (Llama 3.2)

---

## 📂 Project Structure

```
backend/
│
├── llm.py          # Ollama integration
├── database.py     # Mock database
├── tools.py        # API/tool functions
├── agent.py        # Core agent logic
└── main.py         # Entry point
```

---

## ⚙️ Tech Stack

* **Python**
* **Ollama (Llama 3.2)**
* **Requests Library**
* **Virtual Environment (.venv)**

---

## 🔧 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/FINDET-Banking-Fraud-Detection-Agent.git
cd FINDET-Banking-Fraud-Detection-Agent
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install requests
```

---

### 4. Run Ollama (Local LLM)

```
ollama run llama3.2
```

---

### 5. Run the project

```
python backend/main.py
```

---

## 📊 Example Output

```
🧠 Fraud Detection Result:

Risk Level: High  
Reason: Unusual high-value transactions detected  
Recommendation: Flag account and require verification  
```

---

## 🔐 Security Note

* API keys and sensitive data are stored in `.env` (not committed)
* `.gitignore` prevents exposure of secrets

---

## 🚀 Future Enhancements

* ✅ FastAPI backend (REST API)
* ✅ Real-time transaction monitoring
* ✅ Multi-agent system (LangGraph)
* ✅ Dashboard UI (React)
* ✅ Integration with real banking APIs

---

## 💡 Key Learnings

* Agent-based AI system design
* Local LLM integration with Ollama
* Tool calling and data-driven reasoning
* Secure project structuring

---

## 👩‍💻 Author

**Bharti Sahu**
B.Tech CSE | AI & ML Enthusiast

---

## ⭐ Contribute

Feel free to fork this repo, improve it, and submit a PR!

---

## 📌 License

This project is for educational and research purposes.
