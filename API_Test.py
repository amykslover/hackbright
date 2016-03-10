
import json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'category_filter': 'french',
    'term': 'food',
    'limit': 5
}

result = client.search('San Francisco', **params)
print result


# print result.businesses[-2].name
# print result.businesses[-2].rating
# print result.businesses[-2].categories
# print result.businesses[-2].location.display_address
# print result.businesses[-2].location.cross_streets