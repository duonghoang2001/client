import requests
import json
import os

url = 'http://localhost:8069/crm_customer_request/crm_lead'
headers = {'Content-Type': 'application/json'}
dirname = os.path.dirname(os.path.realpath(__file__))
data = json.load(open(os.path.join(dirname, 'lead_data.json')))
data_json = json.dumps(data)
r = requests.post(url=url, data=data_json, headers=headers)