import requests
from requests.auth import HTTPBasicAuth
import json
import os

# Correct endpoint for creating an issue
url = "https://irfanztek.atlassian.net/rest/api/3/issue"

# Fetch the API token from environment variables
api_token = os.getenv("token")
print(api_token)
auth = HTTPBasicAuth("izainula@gmail.com", api_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Correct payload for creating an issue
payload = json.dumps({
    "fields": {
        "project": {
            "key": "TES"
        },
        "summary": "This is a sample issue summary",
        "issuetype": {
            "name": "Task"
        }
    }
})

# Send the request
response = requests.post(
    url,
    data=payload,
    headers=headers,
    auth=auth
)

# Print the response
if response.status_code == 201:  # 201 Created
    print("Issue created successfully:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: {response.status_code} - {response.text}")
