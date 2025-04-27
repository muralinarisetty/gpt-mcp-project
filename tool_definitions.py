weather_tools_metadata = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The city to check."},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "Temperature unit."},
            },
            "required": ["city"],
        },
    }
]

user_tools_metadata = [
    {
        "name": "get_user_profile",
        "description": "Fetch user profile by user ID",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string", "description": "User ID in system."},
            },
            "required": ["user_id"],
        },
    }
]

device_tools_metadata = [
    {
        "name": "restart_device",
        "description": "Restart a hardware device remotely",
        "parameters": {
            "type": "object",
            "properties": {
                "device_id": {"type": "string", "description": "The ID of the device to restart."},
            },
            "required": ["device_id"],
        },
    }
]

functions_metadata = weather_tools_metadata + user_tools_metadata + device_tools_metadata