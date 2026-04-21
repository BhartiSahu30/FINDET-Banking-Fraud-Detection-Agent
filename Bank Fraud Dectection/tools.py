from langchain_core.tools import tool

@tool
def get_user_behavior_profile(user_id: str):
    """
    Retrieves the historical behavioral profile for a specific user.
    Includes home city, risk limits, and unstructured history notes.
    """
    # In a real system, this would query a Vector DB (Chroma/Pinecone) or SQL
    # This mock data is calibrated to test your Agent's RAG capabilities
    profiles = {
        "USER_405": {
            "user_id": "USER_405",
            "home_city": "Bhilai",
            "risk_limit": 10000,
            "trusted_devices": ["iPhone15_Pro", "MacBook_Air"],
            "average_transaction": 1200,
            # This 'notes' field is what proves your Agent has "Advanced RAG" intelligence
            "notes": "User mentioned in a support chat last week they are traveling to Bangalore for a hackathon on April 17th."
        }
    }
    
    return profiles.get(user_id.upper(), {"error": "User profile not found."})

@tool
def check_ip_risk(ip_address: str):
    """
    Checks if a transaction IP address is associated with a VPN, Proxy, or high-risk data center.
    """
    # Mocking technical security tool output
    high_risk_ips = ["45.1.1.1", "103.22.201.5"]
    
    if ip_address in high_risk_ips:
        return {"ip": ip_address, "risk_level": "High", "type": "VPN/Proxy Detected"}
    
    return {"ip": ip_address, "risk_level": "Low", "type": "Residential ISP"}

@tool
def get_last_5_transactions(user_id: str):
    """
    Retrieves the last 5 successful transactions for the user to establish a pattern.
    """
    return [
        {"amount": 500, "location": "Bhilai", "category": "Food"},
        {"amount": 2100, "location": "Bhilai", "category": "Fuel"},
        {"amount": 800, "location": "Bhilai", "category": "Shopping"},
        {"amount": 150, "location": "Bhilai", "category": "Transport"},
        {"amount": 4000, "location": "Bhilai", "category": "Electronics"}
    ]