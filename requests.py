import requests
import json

def main():
    # Prompt the user for a location
    location = input("Enter a location: ")

    # Construct the URL for the API endpoint
    base_url = "http://py4e-data.dr-chuck.net/json?"
    params = {
        "address": location,
        "key": "42"  # Add your API key here if required by the API
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Get the first place_id if available
            if 'results' in data and len(data['results']) > 0:
                place_id = data['results'][0]['place_id']
                print("First place_id:", place_id)
            else:
                print("No results found for the given location.")
        except json.JSONDecodeError:
            print("Error parsing JSON response.")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    main()
