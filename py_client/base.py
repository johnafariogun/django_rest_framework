import requests as r

endpoint = "http://localhost:8000/api/"
getd = r.post(endpoint, json={'name':'laptop', 'price':'23.0', 'type':'electronic device'})
