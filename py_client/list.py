import requests as r

endpoint = 'http://localhost:8000/api/products/'

get_response = r.get(endpoint)
print(get_response.json())
