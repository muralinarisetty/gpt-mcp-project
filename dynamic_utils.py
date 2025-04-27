# utils.py

import importlib
import os
import inspect

# This will be our automatic dispatcher
function_dispatcher = {}

def autoload_functions():
    """Automatically load all functions from tool_handlers folder"""
    handlers_path = "tool_handlers"
    
    for filename in os.listdir(handlers_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{handlers_path}.{filename[:-3]}"  # e.g., tool_handlers.weather_tools
            module = importlib.import_module(module_name)
            
            # Go through all functions in the module
            for name, func in inspect.getmembers(module, inspect.isfunction):
                # Register function
                function_dispatcher[name] = func

def call_function(function_name, arguments):
    """Find and call the correct function with arguments"""
    if function_name not in function_dispatcher:
        raise ValueError(f"Unknown function: {function_name}")
    func = function_dispatcher[function_name]
    return func(**arguments)

# Autoload everything at startup
autoload_functions()
