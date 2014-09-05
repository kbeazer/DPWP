#MADLIB COMIC WORD GAME

'''
This is my first attempt at using python to create a working application.  
I'm still very new to python itself, but I hope you enjoy playing along! :)
'''

#Raw Input is being used to display user name information
user_name = raw_input("Please enter your first name ")

#Display user name along with welcome message
print "Hello " + user_name + ", welcome to the KBeazer Madlib Game!"

#Ensure user is ready to start the game
run_game = raw_input("Press Enter to continue... ")

#Create variable to hold the blank space information
blank_space = "______"

#Build array of words to fill storyline
adj_words = ["smelly","dirty","fancy","playful","sweaty"]

#Build array of numbers for storyline
numbers = ["27","3","34","17","8"]

#Create the Dictionary object to store the storyline information
full_story = dict()

#Populate the dictionary object with user selections
full_story = {"sen_1": "Frank is by far the most original person that you could meet.","sen_2": "He has a total of","sen_3":"pairs of golden jeans.","sen_4":"of those jeans actually belong to the","sen_5":"members of the armed forces of Peru.","sen_6":"They don't mind though, the","sen_7":"year old boss said that it was ok"}

#Create the storyline
print "--------------------------------------------------------------------"
print "Choose the word you think best fills in the blank:"
print blank_space + " " + full_story["sen_1"]

#Create for loop to display array contents
for w in adj_words:
	print w

#Create an array to hold user inputs
answers = []

#User inputs the answer to question 1
ans_1 = raw_input()

#Populate answers array with user input
answers.append(ans_1)

#print answers[0] + " " + full_story["sen_1"]

print "--------------------------------------------------------------------"
print "Choose the word you think best fills in the blank:"
print full_story["sen_2"] + " " + blank_space + " " + full_story["sen_3"]

#Create for loop to display array contents
for n in numbers:
        print n

#User inputs the answer to question 2
ans_2 = raw_input()

#Populate answers array with user input
answers.append(ans_2)

print "--------------------------------------------------------------------"
print "Choose the word you think best fills in the blank:"
print blank_space + " " + full_story["sen_4"] 

#Create for loop to display array contents
for n in numbers:
        print n

#User inputs the answer to question 3
ans_3 = raw_input()

#Populate answers array with user input
answers.append(ans_3)

print "--------------------------------------------------------------------"
print "Choose the word you think best fills in the blank:"
print blank_space + " " + full_story["sen_5"]

#Create for loop to display array contents
for w in adj_words:
        print w

#User inputs the answer to question 4
ans_4 = raw_input()

#Populate answers array with user input
answers.append(ans_4)

print "--------------------------------------------------------------------"
print "Choose the word you think best fills in the blank:"
print full_story["sen_6"] + " " + blank_space + " " + full_story["sen_7"]

#Create for loop to display array contents
for n in numbers:
        print n

#User inputs the answer to question 5
ans_5 = raw_input()

#Populate answers array with user input
answers.append(ans_5)

#Define the printout function
'''
def finResults(f,a):
	results = f + a
	return results

r = finResults(full_story["sen_1"],answers[0])

'''
def finalResults():
	for s in full_story:
		stories = []
		stories.append(full_story[s])
		#return stories
		for a in answers:
			stories += a
			return a
print finalResults()

