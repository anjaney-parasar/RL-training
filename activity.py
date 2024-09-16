# import requests

# url = "https://goagentgomarket.vgtechdemo.com/api/tourism-services"

# response = requests.request("GET", url)

# print(response.text)

import requests

url = "https://goagentgomarket.vgtechdemo.com/api/tourism-services"
def get_tourism_services():
    
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Call the function and print the result
tourism_services = get_tourism_services()
print(tourism_services)
