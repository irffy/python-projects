from flask import Flask 
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

@app.route("/")
def CreateJira():

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
            "summary": "This is a sample issue summary1",
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
    return response.json()


app.run("0.0.0.0",5000)