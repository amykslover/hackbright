import json
import urllib2
import csv
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

COMMAND_CONTINUE = 'c'
COMMAND_SAVE_EXECUTE = 's'
COMMAND_QUIT = 'q'

command_question_dict = {COMMAND_CONTINUE: "continue entering info", COMMAND_SAVE_EXECUTE: "save search and execute", COMMAND_QUIT: "quit without saving"}

def prompt_command():
	for command,prompt in command_question_dict.items():
		print "To", prompt + ', please press', command + "."
	prompt_response = raw_input()
	return prompt_response

def save_search():
	with open("saved_search.txt",'a') as saved_search:
		sv_list = csv.writer(saved_search)
		sv_list.writerow(new_list)
	#with open("saved_search.txt")as saved_search:
	#	print saved_search.read()
	# with open("saved_search.txt")as saved_search:
	# 	lineList = saved_search.readlines()
	# 	print "The last line is: "
	# 	print lineList[-1][0]

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

	return response = client.search(api_list[2], **params)

	

print "Hello! This program will help you find the type of restaurant you want right and save the search for later use. You have three options, type N to create a new search, type E to use a stored search or type Q to quit. "


response = raw_input()
if response == "q":
	print "Goodbye!"
	exit
elif response == "e": 
	print food_file
	saved_request = raw_input("Which saved search do you want to execute? Type the number.")

elif response == "n":
	food_question_count = len(food_question_list) - 1
	for i, item in enumerate(food_question_list):
		new_item = raw_input(item)
		new_list.append(new_item)
		if i < food_question_count:
			current_response = prompt_command()
			if current_response == COMMAND_QUIT:
				print "Goodbye"
				break
				exit
			elif current_response == COMMAND_SAVE_EXECUTE:
				break
			elif current_response == COMMAND_CONTINUE:
				continue
			else:
				print "error"
	save_search()

api_search(new_list)


print response.businesses[0].name, "has a", response.businesses[0].rating, "rating and is located at", response.businesses[0].location.display_address[0], "between", response.businesses[0].location.cross_streets
print response.businesses[1].name, "has a", response.businesses[1].rating, "rating and is located at", response.businesses[1].location.display_address[0], "between", response.businesses[1].location.cross_streets
print response.businesses[2].name, "has a", response.businesses[2].rating, "rating and is located at", response.businesses[2].location.display_address[0], "between", response.businesses[2].location.cross_streets
print response.businesses[3].name, "has a", response.businesses[3].rating, "rating and is located at", response.businesses[3].location.display_address[0], "between", response.businesses[3].location.cross_streets
print response.businesses[4].name, "has a", response.businesses[4].rating, "rating and is located at", response.businesses[4].location.display_address[0], "between", response.businesses[4].location.cross_streets

# category_filter = ""
# radius_filter = 
# limit = 10