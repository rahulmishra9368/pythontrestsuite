import json
import requests
import jsonpath




url = "https://reqres.in/api/users"

'''

file = open('/Users/rahmish2/Documents/test.txt','r')
print(file.read())


'''
file = open('/Users/rahmish2/Documents/data.txt', 'r')
inp = file.read()
req = json.loads(inp)
print(req)

response = requests.post(url,req)
print(response.content)
print(response.status_code)

assert  response.status_code == 201

print(response.headers.get('Content-Type'))

#parse response into json

jsonreppos = json.loads(response.text)
print(jsonreppos)

#validation from response json

date = jsonpath.jsonpath(jsonreppos,'createdAt')
print(date[0])
