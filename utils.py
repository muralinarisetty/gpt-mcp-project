import json
from tool_handlers.weather_tools import get_weather
from tool_handlers.user_tools import get_user_profile
from tool_handlers.device_tools import restart_device

function_dispatcher = {
    "get_weather": get_weather,
    "get_user_profile": get_user_profile,
    "restart_device": restart_device,
}

def call_function(function_name, arguments):
    if function_name not in function_dispatcher:
        raise ValueError(f"Unknown function: {function_name}")
    func = function_dispatcher[function_name]
    return func(**arguments)