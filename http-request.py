import requests

# Using Beekeepers API
base_url = 'https://jsonplaceholder.typicode.com/todos/1'
access_token = 'b1edcre4-d128-4g1a-br5v-a495d00e0j41'
headers = {
    'Authorization': f'Token {access_token}',
    'Accept': 'application/json',
    'Content-type': 'application/json'
}

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed with status code:{response.status_code}.")
