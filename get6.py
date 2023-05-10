import requests # the request module for interacting with APIs
import pprint


url="https://fakerapi.it/api/v1/custom?_quantity=6&customfield1=pokemon&customfield2=website&customfield3=name"


headers={
    "content_type":"application/json"
}

response=requests.get(url=url,headers=headers)

pprint.pprint(response.json())


