import json
import os

BASE_LOCATION = '/workspaces/AI_Gen/dataset'

def read_json_file(filepath):
    """
    Reads data from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict or list: The data loaded from the JSON file, or None if an error occurs.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            print(f"Successfully read data from {filepath}")
            return data
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. Check file format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading {filepath}: {e}")
        return None

deployment_options = {
    "kubernetes": read_json_file(os.path.join(BASE_LOCATION,'aks_price_data.json')),
    "vm": read_json_file(os.path.join(BASE_LOCATION,'vm_price_data.json')),
    "serverless": read_json_file(os.path.join(BASE_LOCATION,'functions_price_data.json'))
}
