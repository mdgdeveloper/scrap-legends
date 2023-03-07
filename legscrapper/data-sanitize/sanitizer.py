import requests

# Basic function to request API 
def get_json_from_api(api_url):
    response = requests.get(api_url)
    json_response = response.json()
    return json_response

