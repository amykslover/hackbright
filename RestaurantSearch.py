import json


print "Hello! This program will help you find the type of restaurant you want right and save the search for later use. You have three options, type N to create a new search, type E to use a stored search or type Q to quit.    "

label = None
saved_search = open("saved_search.txt")
food_type = open("cuisines.txt")
food_file = saved_search.read()
foods = food_type.read()

new_list = []
question_list = ["What type of cuisine? ","How many dollar signs? Enter a number bewteen 1 and 4.  ", "How far away? 1. < 0.25 mile, 2. < 0.5 mile, 3. < 1.0 mile  4. Within city boundaries  "]
price_range = {1: 'inexpensive', 2: 'moderate', 3: 'moderate', 4: 'expensive'}



while label == None:
	response = raw_input()
	if response == "q":
		print "Goodbye!"
	elif response == "n":
		qnumber = 0
		new_item = raw_input(question_list[qnumber])
		#print foods
		new_list.append(new_item)
		second_response = raw_input("Continue entering info? C, Save search and execute? L, Quit without saving? Q   ")
		if second_response == "c":
			qnumber += 1
			new_item = raw_input(question_list[qnumber])
			new_list.append(new_item)
			print new_list
		if second_response == "l":
			new_label = raw_input("Name your search to save and add it to your stored list.   ")	
			print new_label
		if second_response == "q":
			print "Goodbye"			

	elif response == "e": 
		print "Which saved search do you want to execute? Type the number."
		print food_file
	else:
		print "error"

# category_filter = ""
# radius_filter = 
# limit = 10

# Consumer Key	2uVsf-8VUi460QpEt6m5ew
# Consumer Secret	N1hQ7-FlZAe7Oe8vAOxr8xUQ5sc
# Token	TulAFxaEY1PaoD6UWd0jglMJH7mXqRLn
# Token Secret	VMKODcZ0pYU8HYHpa8RprV0EQI0