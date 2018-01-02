#-------Variables and Calculations-----------------

#Assigning variables
scoobySnackServing=5
chaseScenes=2
mysteries=1

#Calculations using variables
totalSnacks=scoobySnackServing*chaseScenes*mysteries

#Printing string variables
print("total Scooby snacks needed is %s" % totalSnacks)

#-------Input----------------------------------------

#Use the input function to prompt the user and assign the typed response
# to a variable.
food=input("Enter a food: ")

print ("You entered %s." % food)

#Prompt the user for a number
# then use int()to convert the string to an integer.
num1=input("Enter a number: ")
num1=int(num1)
print (num1, " times ", num1, " is ", num1*num1)