import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"


data = {
    # 'id' : 18,
    'name' : 'ibrahim',
    'roll' : 18,
    'city': 'goa'
}


json_data = json.dumps(data)

res = requests.post(url= URL, data = json_data)

data = res.json()