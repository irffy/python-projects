import requests
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
# print(response.status_code)

if response.status_code == 200:
    out = response.json()
    # print(out)

    for i in range(len(out)):
        print(out[i]["user"]["login"])
else:
    print(f"Issue with api {response.status_code}")        