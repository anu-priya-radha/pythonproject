import request

url="https://api.github.com/users/anu-priya-radha/repos"

payload={}
headers={}

response = request.request("GET", url, headers = headers, data = payload)

print(response.text)