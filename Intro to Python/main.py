#one lined comments

'''
Doc Strings
'''

first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name  ")
#print "Hello there,", response

birth_year = 1984
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old"

budget = 90
if budget > 100:
	brand = "nike"
	print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 50:
	#print "We can at least get some generic sneakers"
	pass
else:
	#print "No cool shoes for me."
	pass

characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters[1]

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader","Silence of the Lambs":"Hannibal Lector"}
#print movies["Star Wars"]

#WHILE LOOP------
i = 0
while i<9:
	#print "The count is", i
	i+=1

#FOR LOOP-------
for i in range(0,10):
	#print "The count is", i
	i+=1

#FOR EACH LOOP-----
rappers = ["Tupac","Nas","Biggie"]
for r in rappers:
	#print "One of the best rappers is " + r 
	pass

#FUNCTIONS-----------
def calcArea(h,w):
	area = h * w
	return area

a = calcArea(20,40);
#print "My area is " + str(a) + " sqft"


title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
</html>
'''
message = message.format(**locals())
print message
