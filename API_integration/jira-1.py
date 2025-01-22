import requests
import os
from requests.auth import HTTPBasicAuth

api_token = os.getenv("token")
print(api_token)

url = "https://irfanztek.atlassian.net/rest/api/3/project"

headers = {
    "Accept": "application/json"
}
auth = HTTPBasicAuth("izainula@gmail.com", api_token)
response = requests.get(url,headers=headers, auth=auth)
projects = response.json()
# print(projects)
for i in range(len(projects)):
  print(i)  
  project = projects[i]["name"]
  print(project)