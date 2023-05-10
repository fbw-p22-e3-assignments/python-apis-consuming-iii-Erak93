import requests # the request module for interacting with APIs
import pprint


url="https://fakerapi.it/api/v1/persons?_locale=en_EN&_quantity=50&_birthday_start=1994-01-01"


headers={
    "content_type":"application/json"
}

response=requests.get(url=url,headers=headers)

pprint.pprint(response.json())


