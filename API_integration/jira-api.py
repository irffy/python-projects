import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://irfanztek.atlassian.net/rest/api/3/project"

api_token = os.getenv("token")
# print(api_token)
auth = HTTPBasicAuth("izainula@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.get(
   url,
   headers=headers,
   auth=auth
)

output = response.json()
# # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# output = json.loads(response.text)
for i in range(len(output)):
   print(output[i]["name"])
# # print(output)