import json
import urllib2
import csv

from tabulate import tabulate
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


with open("saved_search.txt")as saved_search:
	food_file = saved_search.read()

with open("cuisines.txt")as food_type:
	foods = food_type.read()

with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

new_list = []
food_question_list = ["What type of cuisine? ","What is your price range? cheap, moderate, fancy  ", "Which neighborhood? "]
# price_range = {1: 'inexpensive', 2: 'moderate', 3: 'moderate', 4: 'expensive'}

COMMAND_CONTINUE = 'C'
COMMAND_SAVE_EXECUTE = 'S'
COMMAND_QUIT = 'Q'

command_question_dict = {COMMAND_CONTINUE: "Continue entering search terms?", COMMAND_SAVE_EXECUTE: "Save search and execute search?", COMMAND_QUIT: "Quit without saving?"}

def prompt_command():
	for command,prompt in command_question_dict.items():
		print prompt , 'Press', command + "."
	prompt_response = raw_input().upper()
	print('')
	return prompt_response

def save_search():
	with open("saved_search.txt")as saved_search:
		last_index = saved_search.readlines()
		n = [int(last_index[-1][0])+1]

	with open("saved_search.txt",'a') as saved_search:
		sv_list = csv.writer(saved_search)
		sv_list.writerow(n + new_list)


def api_search(api_list):
	with open('config_secret.json') as cred:
	    creds = json.load(cred)
	    auth = Oauth1Authenticator(**creds)
	    client = Client(auth)

	params = {
	    'category_filter': api_list[0].lower(),
	    'term': api_list[1].lower(),
	    'limit': 5
	    }
	response = client.search(api_list[2], **params) #need to add "San Francisco as default here"
	return response
	

#Program starts here:

print "Hello! This program will help you find the type of restaurant you want right and save the search for later use."
print('')
print "You have three options:"
print "Enter N to create a new search."
print "Enter E to use a stored search."
print "Enter Q to quit."
print('')

user_response = raw_input().lower()

if user_response == "q":
	print('')
	print "Goodbye!"
	exit

elif user_response == "e":

	temp_list = []

	with open("saved_search.txt", 'r') as f:
		food_file = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in food_file:
			temp_list.append(row)

		headers=['Number', 'Cuisine', 'Price Range', 'Neighborhood' ]
		print tabulate(temp_list, headers, tablefmt='orgtbl')
		print " "
	
	saved_request = raw_input("Which saved search do you want to execute? Type the number.")
	print('')
	exist_list = temp_list[int(saved_request)-1][1:]

	print "The seach terms for this query are:"
	print " "
	print tabulate([exist_list], headers=['Cuisine', 'Price', 'Location' ], tablefmt='orgtbl')
	response = api_search(exist_list)
	print('')
# Returns results of API call
	print "Your results are:"
	print " "
	rest1 = response.businesses[0].name, response.businesses[0].rating, response.businesses[0].location.display_address[0], response.businesses[0].location.cross_streets
	rest2 = response.businesses[1].name, response.businesses[1].rating, response.businesses[1].location.display_address[0], response.businesses[1].location.cross_streets
	rest3 = response.businesses[2].name, response.businesses[2].rating, response.businesses[2].location.display_address[0], response.businesses[2].location.cross_streets
	rest4 = response.businesses[3].name, response.businesses[3].rating, response.businesses[3].location.display_address[0], response.businesses[3].location.cross_streets
	rest5 = response.businesses[4].name, response.businesses[4].rating, response.businesses[4].location.display_address[0], response.businesses[4].location.cross_streets
	table = [rest1, rest2, rest3, rest4, rest5]
	headers=['Restaurant Name', 'Rating', 'Address', 'Cross Streets' ]
	
	print tabulate(table, headers, tablefmt='orgtbl')


elif user_response == "n":
	food_question_count = len(food_question_list) - 1
	for i, item in enumerate(food_question_list):
		new_item = raw_input(item)
		print('')
		new_list.append(new_item)
		if i < food_question_count:
			current_response = prompt_command()
			if current_response == COMMAND_QUIT:
				print "Goodbye"
				# break
				exit
			elif current_response == COMMAND_SAVE_EXECUTE:
				break
			elif current_response == COMMAND_CONTINUE:
				continue
			else:
				print "error"
	save_search()
	print "The seach terms for this query are:"
	print " "
	print tabulate([new_list], headers=['Cuisine', 'Price', 'Location' ], tablefmt='orgtbl')
	response = api_search(new_list)
	print " "
	print " "

# Returns results of API call
	print "Your results are:"
	print " "
	rest1 = response.businesses[0].name, response.businesses[0].rating, response.businesses[0].location.display_address[0], response.businesses[0].location.cross_streets
	rest2 = response.businesses[1].name, response.businesses[1].rating, response.businesses[1].location.display_address[0], response.businesses[1].location.cross_streets
	rest3 = response.businesses[2].name, response.businesses[2].rating, response.businesses[2].location.display_address[0], response.businesses[2].location.cross_streets
	rest4 = response.businesses[3].name, response.businesses[3].rating, response.businesses[3].location.display_address[0], response.businesses[3].location.cross_streets
	rest5 = response.businesses[4].name, response.businesses[4].rating, response.businesses[4].location.display_address[0], response.businesses[4].location.cross_streets
	table = [rest1, rest2, rest3, rest4, rest5]
	headers=['Restaurant Name', 'Rating', 'Address', 'Cross Streets' ]
	
	print tabulate(table, headers, tablefmt='orgtbl')

