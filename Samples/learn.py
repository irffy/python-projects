# # # # txt = "Hello World Python"
# # # # print(txt)
# # # # x = " ".join(txt.split()[::-1])
# # # # print(x)

# # # n = int(input("Enter a number:"))

# # # for i in range(1,n+1):
# # #     # print(i)
# # #     j=""
# # #     if i%3 ==0:
# # #         j+="Irfan"
# # #     if i%5 ==0:
# # #         j+="Ahmed"
# # #     if i%7 ==0:
# # #         j+="Zainulabdin"   
# # #     if j:
# # #       print(j)
# # #     else:
# # #       print(i)      
           
# # def test(n):
# #     print("Hello Irfan!!")
# #     return n

# # @test
# # def hi():
# #    print("Hello World!!")          

# # hi()

# # import requests
# # import os
# # from requests.auth import HTTPBasicAuth

# # url = "https://irfanztek.atlassian.net/rest/api/3/project"
# # token = os.getenv("token")
# # auth = HTTPBasicAuth("izainula@gmail.com",token)
# # headers = {
# #     "Accept": "application/json"
# # }

# # response = requests.get(url,auth=auth,headers=headers)
# # print(response)
# # out = response.json()
# # print(out)

# import requests
# from requests.auth import HTTPBasicAuth
# import json
# import os

# url = "https://irfanztek.atlassian.net/rest/api/3/project"

# api_token = os.getenv("token")
# # print(api_token)
# auth = HTTPBasicAuth("izainula@gmail.com", api_token)

# headers = {
#   "Accept": "application/json"
# }

# response = requests.get(
#    url,
#    headers=headers,
#    auth=auth
# )

# # output = response.json()
# output = json.loads(response.text)
# print(output)

import requests
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
# print(response.status_code)

if response.status_code == 200:
    out = response.json()
    print(out)

    for i in range(len(out)):
        print(out[i]["user"]["login"])
else:
    print(f"Issue with api {response.status_code}")        