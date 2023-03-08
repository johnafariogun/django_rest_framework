import requests as r
p_id = input('enter an id to be deleted\n')
try:
    id_ = int(p_id)
except:
    id_ = None
    print(f'{p_id} enter valid id')
if id_:    
    endpoint = f"http://localhost:8000/api/products/{id_}/delete/"

    get_response = r.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)