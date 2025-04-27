import requests

MCP_SERVER_URL = "http://localhost:5000"

def get_user_profile(user_id: str) -> str:
    response = requests.post(f"{MCP_SERVER_URL}/user_profile", json={"user_id": user_id})
    response.raise_for_status()
    return response.json().get("profile_summary", "No user found.")