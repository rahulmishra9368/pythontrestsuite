import json
import requests
import jsonpath








def test_updateuser():
  url = "https://reqres.in/api/users"
  file = open('/Users/rahmish2/Documents/data.txt', 'r')
  inp = file.read()
  req = json.loads(inp)
  print(req)
  response = requests.post(url,req)
  #print(response.content)
  #print(response.status_code)
  assert  response.status_code == 201
  #print(response.headers.get('Content-Type'))
  #parse response into json
  jsonreppos = json.loads(response.text)
  print(jsonreppos)
  #validation from response json
  date = jsonpath.jsonpath(jsonreppos,'createdAt')
  print(date[0])



def test_upteuser():
  url = "https://reqres.in/api/users"
  file = open('/Users/rahmish2/Documents/data.txt', 'r')
  inp = file.read()
  req = json.loads(inp)
  print(req)
  response = requests.post(url,req)
  #print(response.content)
  #print(response.status_code)
  assert  response.status_code == 201
  #print(response.headers.get('Content-Type'))
  #parse response into json
  jsonreppos = json.loads(response.text)
  print(jsonreppos)
  #validation from response json
  date = jsonpath.jsonpath(jsonreppos,'createdAt')
  print(date[0])


def test_updateusr():
  url = "https://reqres.in/api/users"
  file = open('/Users/rahmish2/Documents/data.txt', 'r')
  inp = file.read()
  req = json.loads(inp)
  print(req)
  response = requests.post(url,req)
  #print(response.content)
  #print(response.status_code)
  assert  response.status_code == 204
  #print(response.headers.get('Content-Type'))
  #parse response into json
  jsonreppos = json.loads(response.text)
  print(jsonreppos)
  #validation from response json
  date = jsonpath.jsonpath(jsonreppos,'createdAt')
  print(date[0])