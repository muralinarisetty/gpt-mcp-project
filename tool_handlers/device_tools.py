import requests

MCP_SERVER_URL = "http://localhost:5000"

def restart_device(device_id: str) -> str:
    response = requests.post(f"{MCP_SERVER_URL}/restart_device", json={"device_id": device_id})
    response.raise_for_status()
    return response.json().get("status", "Unknown device status.")