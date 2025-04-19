import requests
import json
import os

# Base URL for the Azure Retail Prices API
AZURE_PRICING_API_URL = "https://prices.azure.com/api/retail/prices"

# Base Location for storing dataset
BASE_LOCATION = os.path.expanduser('/workspaces/AI_Gen/dataset')

# --- Filters for specific service types using serviceName ---

# Filter for Virtual Machines using serviceName
# Still adding location, priceType, and unitOfMeasure for specificity
VM_FILTER_SN = "serviceName eq 'Virtual Machines' and priceType eq 'Consumption' and unitOfMeasure eq '1 Hour'" # Example location

# Filter for Azure Kubernetes Service using serviceName
# Still adding location and priceType
AKS_FILTER_SN = "serviceName eq 'Azure Kubernetes Service' and priceType eq 'Consumption' and unitOfMeasure eq '1 Hour'" # Example location

# Filter for Azure Functions using serviceName
# Still adding location and priceType
FUNCTIONS_FILTER_SN = "serviceName eq 'Functions' and priceType eq 'Consumption' and unitOfMeasure eq '1 Hour'" # Example location

def fetch_azure_prices(filter_query, service_description):
    """Fetches prices from Azure Retail Prices API based on a filter query."""
    query_url = f"{AZURE_PRICING_API_URL}?$filter={filter_query}"
    print(f"Attempting to fetch {service_description} prices from: {query_url}")

    try:
        response = requests.get(query_url)
        response.raise_for_status() # Raise an exception for bad status codes

        data = response.json()
        items = data.get('Items', [])

        if not items:
            print(f"No items found for the {service_description} query.")
            return []

        print(f"Found {len(items)} items for {service_description} (displaying first 10):")
        # In a real application, you might need to handle pagination
        # with data.get('@odata.nextLink')

        return items

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {service_description} prices: {e}")
        # print(f"Response body: {response.text}") # Uncomment for debugging API errors
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON response from API for {service_description}.")
        return None
def format_json(item):
    return {
        'serviceName': item.get('serviceName'),
        'product': item.get('productName'),
        'meterName': item.get('meterName'),
        'price': item.get('unitPrice'),
        'location': item.get('location')
    }


def save_to_json_file(data, filename):
    """Saves data to a JSON file in the specified directory."""
    filepath = os.path.join(BASE_LOCATION, filename)

    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully saved data to {filepath}")
    except IOError as e:
        print(f"Error saving data to {filepath}: {e}")

# --- Main execution ---
if __name__ == "__main__":

    # Fetch and display VM Prices using serviceName
    vm_prices = fetch_azure_prices(VM_FILTER_SN, "Azure VMs (using serviceName filter)")
    
    if vm_prices:
        print("\n--- Sample Azure VM Prices (East US) ---")
        formatted_vm_prices = []
        for i, item in enumerate(vm_prices): # Displaying top 5 results
            formatted_vm_prices.append(format_json(item))
        save_to_json_file(formatted_vm_prices, 'vm_price_data.json')
        print("\n(Note: Filtered by serviceName eq 'Virtual Machines', Consumption, hourly unit.)")


    # Fetch and display AKS Service Fee Prices using serviceName
    aks_prices = fetch_azure_prices(AKS_FILTER_SN, "Azure AKS Service Fee (using serviceName filter)")
    if aks_prices:
        print("\n\n--- Sample Azure AKS Service Fee Prices (East US) ---")
        formatted_aks_prices =[]
        for i, item in enumerate(aks_prices):
             formatted_aks_prices.append(format_json(item))
        save_to_json_file(formatted_aks_prices, 'aks_price_data.json')
        print("\n(Note: Filtered by serviceName eq 'Azure Kubernetes Service', Consumption price type. This is for the AKS cluster management/SLA fee.)")


    # Fetch and display Azure Functions Consumption Prices using serviceName
    functions_prices = fetch_azure_prices(FUNCTIONS_FILTER_SN, "Azure Functions Consumption Plan (using serviceName filter)")
    if functions_prices:
        print("\n\n--- Sample Azure Functions Consumption Plan Prices (East US) ---")
        formatted_functions_prices = []
        for i, item in enumerate(functions_prices):
            formatted_functions_prices.append(format_json(item))
        save_to_json_file(formatted_functions_prices, 'functions_price_data.json')
        print("\n(Note: Filtered by serviceName eq 'Azure Functions', Consumption price type. Look for meters related to execution count and execution time/memory.)")

    print("\n--- Using this data for your Hackathon ---")
    print("Using 'serviceName' provides a good level of filtering for these specific services.")
    print("You can use the 'retailPrice' and 'unitOfMeasure' from the results to inform your static costs.")
    print("Remember you still need to identify specific SKUs/meters and estimate usage for your scenarios.")