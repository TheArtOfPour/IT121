import sys

#Gather some data

print ("How many zombies are there?: ", end="")

zombieCount=int(sys.stdin.readline())
 

print("\nThere are %s zombies." % zombieCount)
 

#Make a decision based on the data

#Use IF statements

# if something is true:

# do all the things indented under it
 

if zombieCount > 2 :

   print("\nRun!")

   # all commands indented in this block will run

   print("Gather friends.")

   print("Gather weapons.")

 

#An unindented line ends the block

print("Find a defensible position.")

 

print ("\nHow many friends are there?: ", end="")

friendCount=int(sys.stdin.readline())

 

#Some different symbols for conditions

if friendCount > zombieCount:

   print ("You have more friends than zombies.")

 

if friendCount < zombieCount:

   print ("You have fewer friends than zombies.")

 

if friendCount == zombieCount:

   print ("You have the same number of friends as zombies.")

 

if friendCount != zombieCount:

   print ("You do not have the same number of friends as zombies.")

 

if friendCount >= zombieCount:

   print ("You have at least as many friends as zombies.")

 

if friendCount <= zombieCount:

   print ("You do not have more friends than zombies.")

 

print("\n\n")

 

#Using ELSE when the IF condition is false

if zombieCount < friendCount:

   print ("Fight")

else:

   print ("Run")

 

print("\n\n")

 

#Using ELSIF to check for more than two alternatives

#Start low and work up or start high and work down in your comparisons

if zombieCount < 2:

   print ("You have a zombie.")

elif zombieCount < 3:

   print ("You have a couple of zombies.")

elif zombieCount < 5:

   print("You have a few zombies.")

elif zombieCount < 12:

   print("You have several zombies.")

elif zombieCount < 100:

   print("You have dozens of zombies.")

else:

   print("You have hundreds of zombies.")

 

print("\n\n")

 

#Combining conditions with AND and OR

print ("\nAre the zombies fast?(y/n): ", end="")

zombiesFast=sys.stdin.readline()

zombiesFast=zombiesFast.rstrip()

 

#AND means both conditions need to be true

if friendCount > zombieCount and zombiesFast != "y":

   print("You have more friends than slow zombies so fight.")

else:

   print("Run")

 

print("\n\n")

 

#OR means only one of the conditions needs to be true

if friendCount < zombieCount or zombiesFast == "y":

   print("Run")

else:

   print("You have more friends than slow zombies so fight.")

 

#Compare two strings

print ("\nEnter the first string: ", end="")

stringOne=sys.stdin.readline()

stringOne=stringOne.rstrip()

 

print ("\nEnter the second string: ", end="")

stringTwo=sys.stdin.readline()

stringTwo=stringTwo.rstrip()

 

if stringOne > stringTwo:

   print ("%s > %s" % (stringOne,stringTwo))

if stringOne < stringTwo:

   print ("%s < %s" % (stringOne,stringTwo))

 

#fun with IF statements and sounds
import winsound

animal=input("What animal would you like to hear? ")

cats=("cat","Cat","CAT","Siamese","pest")

# Compare to input
if animal == "seagull":
winsound.PlaySound("assets/seagull.wav",0)

# check if in a list
elif animal in ("dog","Dog","DOG"):
winsound.PlaySound("assets/dog.wav",0)

elif animal in cats:
winsound.PlaySound("assets/cat.wav",0)

# build the filename
animal="assets/"+animal+".wav"

import os.path
if os.path.isfile(animal):

winsound.PlaySound(animal,0)
else:
print (animal, "does not exist.")