
import json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'term': 'food',
}

result = client.search('San Francisco', **params)

print result.businesses[0].name
print result.businesses[0].rating
