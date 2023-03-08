import requests as r

endpoint = 'http://localhost:8000/api/products/'
data = {
    'name':'infinix zero',
    'type':'android phone',
    'price': 34,
    'content': "generate random text"
    }
get_response = r.post(endpoint, json=data)
print(get_response.json())