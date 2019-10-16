import requests
import json
import jsonpath
import logging




url = "https://reqres.in/api/users?page=2"

#getting response
resp = requests.get(url)
#print(resp)

#print(resp.content)
#print(resp.headers)

#json response


json_resp = json.loads(resp.text)
#print(json_resp)


#fetch specific value

pages = jsonpath.jsonpath(json_resp,'total_pages')
#print(pages[0])

assert pages[0] == 2
logging.info('test')


