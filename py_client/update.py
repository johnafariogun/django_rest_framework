import requests as r
endpoint = 'http://localhost:8000/api/products/7/update/'
data = {
    'name':'redmi note 8',
    'type':'android xiaomi mobile phone',
    'price':34
}
get_response = r.put(endpoint, json=data)
print(get_response.json())