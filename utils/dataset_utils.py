import json
import os
from sentence_transformers import SentenceTransformer, util

# Load once at top level
model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight & fast

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

def location_similarity(loc1: str, loc2: str, threshold: float = 0.7) -> bool:
    """
    Returns True if cosine similarity between loc1 and loc2 ≥ threshold.
    """
    embedding1 = model.encode(loc1, convert_to_tensor=True)
    embedding2 = model.encode(loc2, convert_to_tensor=True)
    similarity = util.cos_sim(embedding1, embedding2).item()
    return similarity >= threshold

def filter_deployments(service_key: str, user_input: dict, max_items: int = 5):
    """
    Filter deployments[service_key] based on user_input:
    - 'max_budget' : float
    - 'location' : string (optional)

    Returns up to `max_items` matching options.
    """
    raw_data = deployment_options.get(service_key, [])
    filtered = []

    for item in raw_data:
        if "max_budget" in user_input and item["price"] > user_input["max_budget"]:
            continue
        if "location" in user_input and user_input['location'] is not None:
            user_loc = user_input["location"]
            dataset_loc = item["location"]
            if not location_similarity(user_loc, dataset_loc):
                continue
        filtered.append(item)

    return sorted(filtered, key=lambda x: x["price"])[:max_items]
