import requests # the request module for interacting with APIs
import pprint


url="https://fakerapi.it/api/v1/companies?_quantity=5&_locale=de_DE"


headers={
    "content_type":"application/json"
}

response=requests.get(url=url,headers=headers)

pprint.pprint(response.json())


