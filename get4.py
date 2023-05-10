import requests # the request module for interacting with APIs
import pprint


url="https://fakerapi.it/api/v1/credit_cards?_quantity=60&_locale=es_ES"


headers={
    "content_type":"application/json"
}

response=requests.get(url=url,headers=headers)

pprint.pprint(response.json())


