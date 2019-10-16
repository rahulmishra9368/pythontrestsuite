import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open('/Users/rahmish2/Documents/data.txt','r')

jsoninput = file.read()
reqjjson = json.loads(jsoninput)

response = requests.put(url,reqjjson)

response_json = json.loads(response.text)


print(response.status_code)
print(response.content)


assert  response.status_code == 200

updatedli = jsonpath.jsonpath(response_json,'updatedAt')
print(updatedli[0])
