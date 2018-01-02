#------- Lists --------------------
# A list is a collection of values. You create the list with square brackets.

mysteryInc=['Velma','Scooby','Daphne','Shaggy','Fred']
print (mysteryInc)

# You can refer to items in a list by using their positions, called an index.
# Index numbering starts with 0.

print ("Index 0 refers to ", end="")
print (mysteryInc[0])

print ("Index 3 refers to ", end="")
print (mysteryInc[3])

# You can refer to subsets in a list.
# The first number is where you start printing,
# the second number is where you stop printing. You don't print the stop index.

print ("\nStart at index 1 and stop when you reach 4.")
print (mysteryInc[1:4])

# You can add items to a list using the list.append() function.

mysteryInc.append("Mister E");
print ("\nThe new list after adding Mister E:")
print (mysteryInc)

# You can remove items from a list using the del list[idx] command.
# Specify which index number you want to delete.

del mysteryInc[4]
print ("\nThe new list after removing item 4 is:")
print (mysteryInc,"\n\n")

#-------Tuples---------------------
# A tuple like a list in that it is a collection of items.
# It is unlike a list in that it can contain things that are not like each other,
# it cannot be changed, and it uses parentheses instead of square brackets.

# For example a tuple could contain a transaction, which could be made up of
# a serial number and a name and a dollar amount and a time.

# A list would be good for storing a bunch of names you want to access individually.
# A tuple would be good for storing a transaction whose different pieces have meaning
# only when you look at them all together.

# A list is an updatable collection of simple similar things.
# A tuple is an unchanging set of dissimilar things, that often describe one complex thing.

# The localtime() function returns a tuple.
print ("The local time function returns a tuple containing all the components:")
import time
print (time.localtime(), "\n\n")

#-------Maps or Dictionaries--------------
# A map or dictionary in python is a collection of pairs. The first part of
# the pair is the key and the second part of the pair is its corresponding value.
# Maps use braces, {}, to define them.

hobbies={'Fred' : 'traps',
'Velma' : 'books',
'Daphne' : 'fashion',
'Shaggy' : 'food',
'Scooby' : 'food'}
print ("The hobbies map looks like this ")
print (hobbies)

# Use the key to get to the value.
# You still use square braces for the key, like the index to a list.

print ("\nFred\'s hobby is %s.\n" % hobbies['Fred'])

# You can add to a map by assigning a value to a new key.

hobbies['Mike'] = 'Amphibian surveying'
print ("\n After adding 'Mike':'Amphibian surveying' the hobbies map looks like this ")
print (hobbies)

# You can delete a map pair by deleting the key.
del hobbies['Shaggy']
print ("\n After deleting hobbies['Shaggy'] the hobbies map looks like this ")
print (hobbies)

#------- Homework Example ----------
# Asking the user to enter a map pair could look something like this:
# Prompt the user for a name.
# Get the name from the user.
inName = input("\n\nEnter a name: ")
# Strip the newline off the input.
inName = inName.rstrip()

# Get a hobby from the user.
inHobby = input("\n\nEnter a hobby: ")
# Strip the newline off the input.
inHobby = inHobby.rstrip()

# Add the new pair to the map
hobbies[inName] = inHobby

# Print the new map
print ("\n\nAfter adding %s:%s the new hobby map looks like this " % (inName,inHobby))
print (hobbies)

# Get the name from the user again to do a lookup.
inName = input("\n\nEnter a name: ")
# Strip the newline off the input.
inName = inName.rstrip()

print ("%s's hobby is %s." % (inName, hobbies[inName]))