import os
import re
from typing import Literal
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from state import AgentState

# --- 1. Import your custom tool ---
# Make sure your function in tools.py is named check_transaction_history
try:
    from tools import check_transaction_history
except ImportError:
    # Fallback if the file isn't found during testing
    def check_transaction_history(user_id):
        return {"avg_spend": 100, "typical_location": "Unknown", "status": "No Data"}

# --- 2. Setup LLM ---
llm = ChatOllama(model="llama3.2", temperature=0)

# --- 3. Define the Nodes ---

def fetch_data_node(state: AgentState):
    """
    Node 1: Fetches background data.
    We'll extract a User ID from the last message or use a default.
    """
    # Logic to find a User ID if present, otherwise default
    user_id = "USER_9921" 
    
    # Call your tool
    history = check_transaction_history(user_id)
    
    # We return the dictionary to update 'user_history' in AgentState
    return {"user_history": history}

def investigator(state: AgentState):
    """
    Node 2: The AI Analyst.
    Now it uses BOTH the message and the history we just fetched.
    """
    last_message = state['messages'][-1].content
    history = state.get("user_history", {})
    
    # The "Smart" Prompt using retrieved data
    prompt = (
        "You are a Fraud Detection Expert.\n"
        f"CUSTOMER HISTORY: Typical spend ${history.get('avg_spend', 'Unknown')}, "
        f"Location: {history.get('typical_location', 'Unknown')}.\n"
        f"NEW TRANSACTION: {last_message}\n\n"
        "Compare the new transaction to the history. "
        "Output ONLY a risk score between 0.0 and 1.0."
    )
    
    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        match = re.search(r"[-+]?\d*\.\d+|\d+", content)
        score = float(match.group()) if match else 0.5
    except:
        score = 0.5
        
    return {"risk_score": score}

def approve_node(state: AgentState):
    return {"messages": [AIMessage(content="✅ APPROVED: Transaction matches user profile.")]}

def block_node(state: AgentState):
    return {"messages": [AIMessage(content="❌ BLOCKED: Significant deviation from user history.")]}

def review_node(state: AgentState):
    return {"messages": [AIMessage(content="⚠️ REVIEW: Unusual patterns, requires human verification.")]}

# --- 4. Routing Logic ---
def router(state: AgentState) -> Literal["approve", "block", "review"]:
    score = state.get("risk_score", 0.5)
    if score < 0.3: return "approve"
    elif score > 0.7: return "block"
    else: return "review"

# --- 5. Construct the Graph ---
builder = StateGraph(AgentState)

# Add Nodes
builder.add_node("fetcher", fetch_data_node)
builder.add_node("investigator", investigator)
builder.add_node("approve", approve_node)
builder.add_node("block", block_node)
builder.add_node("review", review_node)

# Define the Flow (The "Wires")
builder.set_entry_point("fetcher")      # 1. Start with the Tool
builder.add_edge("fetcher", "investigator") # 2. Move to AI Analysis

# 3. Conditional routing based on the score
builder.add_conditional_edges(
    "investigator",
    router,
    {
        "approve": "approve",
        "block": "block",
        "review": "review"
    }
)

builder.add_edge("approve", END)
builder.add_edge("block", END)
builder.add_edge("review", END)

graph = builder.compile()