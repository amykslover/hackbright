import json
import urllib2
import csv

with open("saved_search.txt")as saved_search:
	food_file = saved_search.read()

with open("cuisines.txt")as food_type:
	foods = food_type.read()

label = None
new_list = []
food_question_list = ["What type of cuisine? ","How many dollar signs? Enter a number bewteen 1 and 4.  ", "How far away? 1. < 0.25 mile, 2. < 0.5 mile, 3. < 1.0 mile  4. Within city boundaries  "]
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
	with open("saved_search.txt",'a')as saved_search:
		sv_list = csv.writer(saved_search)
		sv_list.writerow(new_list)
	with open("saved_search.txt")as saved_search:
		print saved_search.read()


print "Hello! This program will help you find the type of restaurant you want right and save the search for later use. You have three options, type N to create a new search, type E to use a stored search or type Q to quit. "


response = raw_input()
if response == "q":
	print "Goodbye!"
elif response == "e": 
	print "Which saved search do you want to execute? Type the number."
	print food_file
elif response == "n":
	food_question_count = len(food_question_list) - 1
	for i, item in enumerate(food_question_list):
		new_item = raw_input(item)
		new_list.append(new_item)
		if i < food_question_count:
			current_response = prompt_command()
			if current_response == COMMAND_QUIT:
				print "Goodbye"
				exit
			elif current_response == COMMAND_SAVE_EXECUTE:
				break
			elif current_response == COMMAND_CONTINUE:
				continue
			else:
				print "error"
	save_search()
		
	# 	if second_response == "c":
	# 		qnumber += 1
	# 		new_item = raw_input(question_list[qnumber])
	# 		new_list.append(new_item)
	# 		print new_list
	# 	if second_response == "l":
	# 		new_label = raw_input("Name your search to save and add it to your stored list.   ")	
	# 		print new_label
	# 	if second_response == "q":
	# 		print "Goodbye"			

	# else:
	# 	print "error"

# category_filter = ""
# radius_filter = 
# limit = 10