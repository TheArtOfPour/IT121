import sys
import turtle
t=turtle.Pen()
t.reset()
t.speed(10)

#A function is a set of commands given a name.
def drawASquare():
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)

#A function does nothing unless you "call" it.
#Uncomment the following lines to run the drawASquare function.

#drawASquare()
#t.up()
#t.forward(200)
#t.down()
#drawASquare()

#Functions and loops work well together to perform repetitive tasks with
# a few lines of programming code.
#Uncomment the following lines to draw a pattern.

#t.reset()
#for x in range(0,18):
#   drawASquare()
#   t.left(20)
#   t.up()
#   t.forward(10)
#   t.down()

# A sample function that takes input and echoes it.
def testFunction(parameter1, parameter2, parameter3):
    print ("parameter1 is %s" % parameter1)
    print ("parameter2 is %s" % parameter2)
    print ("parameter3 is %s\n" % parameter3)

#Using a function is often referred to as "calling" the function.
#This example passes strings to the function.
testFunction("a","b","c")

#This example passes numbers to the function.
testFunction(1,2,3)

#This example assigns numbers to variables and passes the variables to the function.
param1 = 25
param2 = 624
param3 = 8675309

testFunction(param1,param2,param3)


# Uncomment either of these function calls to see that the parameter count
# needs to match

#testFunction("1","2")
#testFunction("a","b","c","e")

#Functions do work. They can also receive input via parameters,
# or they can return a result, or both receive and return.
def gradeTranslator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print ("Score: 77 = Grade: %s" % (gradeTranslator(77)))
print ("Score: 88 = Grade: %s" % (gradeTranslator(88)))


#Functions make programs that interact with the user simpler.

#Line drawing function
def drawALine(direction,length):
    t.setheading(direction)
    t.forward(length)

#Asking function
def getInfo():
    print ("What direction to point? (1-360) (0=quit): ", end="")
    direction = int(sys.stdin.readline())
    if direction != 0:
        print ("How far to draw?: ", end="")
        length = int(sys.stdin.readline())
    else:
        length = 0

    return (direction, length)

 

#Main Program
while True:
    direction,length = getInfo()
    if direction == 0:
        break
    else:
        drawALine(direction,length)
