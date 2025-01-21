import requests

project = input("Enter github project name:")
repo = input("Enter github project repo name:")
url = f'https://api.github.com/repos/{project}/{repo}/pulls'

print(url)
response = requests.get(url)
# print(response)
response_json = response.json()
# print(response_json)
if response.status_code == 200:
    for i in range(len(response_json)):
        # print(f"========={i}=========")
        print(response_json[i]['user']['login'])
else:
    error_message = response.json().get('message')
    print(f"Something wrong!!  - {response.status_code} {error_message}")    