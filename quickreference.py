#variables are used to define, change and redefine values
print("\nVARIABLES")
myVariable="Doge"
otherVariable="Much"


#print is a function used to output text to the console
print("\nPRINT")
print(myVariable)
#end can be specified to override the default \n newline character
print('Inject variables using %', end="")
#variables can be printed in a string using "%s"
print('s %s %s Such Wow' % (myVariable, otherVariable))
#\n = newline
#\t = tab
#%s = string placeholder
#%d = numeric placeholder
#%f = float placeholder


#input is a function used to collect user defined content from the console
print("\nINPUT")
favoriteFood=input("What's your favorite food? ")
print("Really, you like %s?" % favoriteFood)


#calculations
# + - * /
print("\nCALCULATIONS")
miles=40
hours=2
cars=input("How many cars are driving? ")
cars=int(cars)
mph=(miles/hours)
combinedmph=(miles/hours)*cars
print("%d cars at %dmph are going %d" % (cars,mph,combinedmph))


#strings
# ' " '''
print("\nSTRINGS")
print('And she said "Aren\'t you glad I didn\'t say banana?"')
print("And she said \"Aren't you glad I didn't say banana?\"")
print('''And she said "Aren't you glad I didn't say banana?"''')


#tuples can not be modified but can contain different types
# ()
print("\nTUPLES")
contactTuple=('555-5555','test@email.com',4)
print('Call me at %s or email me at %s after %dpm' % contactTuple)


#lists can be modified but must consist of the same types
# []
print("\nLISTS")
groceryList=['Bears','Beets','Battlestar','Cylons']
print(groceryList)
del groceryList[3]
print(groceryList)
groceryList.append('Galactica')
print(groceryList)
print('The last thing on the list is %s' % groceryList[len(groceryList)-1])


#maps are like lists, but consist of key/value pairs
# {}
print("\nMAPS")
contactMap={
    'Ed':('123-4567','ed@aol.com',3),
    'Edd':('867-5309','edd@hotmail.com',1),
    'Eddy':('777-8888','eddy@btc.edu',0)
    }
print('Call Ed at %s or email Ed at %s after %dpm' % contactMap['Ed'])
print('Call Edd at %s or email Edd at %s after %dpm' % contactMap['Edd'])
print('Call Eddy at %s or email Eddy at %s after %dpm' % contactMap['Eddy'])


#import allows the inclusion of modules for additional functionality
print("\nIMPORT")
import time as t
time=t.time()
localtime=t.localtime(time)
formattedtime=t.asctime(localtime)
print("Local current time : %s" % formattedtime)

      
#turtle is a vector based drawing module
# forward(x) moves the turtle forward x pixels
# left(a)/right(a) turns the turtle a degrees
# up()/down() pulls the pen up or puts it down, while up the turtle won't draw
# goto(x,y) warps the turtle to the coordinates pair (x,y)
print("\nTURTLE")
print("This should open a new window")
import turtle as tu
import random as rn
def draw_star(x, y, color, side):
    tu.color(color)
    tu.begin_fill()
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    for k in range(5):
        tu.forward(side)
        tu.right(144)
        tu.forward(side)
    tu.end_fill()
def random_length():
    return rn.randrange(5, 25)
def random_xy_coord():
    return rn.randrange(-290, 290), rn.randrange(-270, 270) 
tu.title('a star filled sky')
tu.bgcolor('black')
# optional ('normal' is default) ...
# values for speed are 'fastest' (no delay), 'fast', (delay 5ms),
# 'normal' (delay 10ms), 'slow' (delay 15ms), 'slowest' (delay 20ms)
tu.speed('fastest')
colors = ['red', 'orange', 'magenta', 'green', 'blue', 'yellow', 'white']
# number of stars you want to show
stars = 50
for k in range(stars):
    color = rn.choice(colors)
    side = random_length()  # length of side
    x, y  = random_xy_coord()
    draw_star(x, y, color, side)
# keep showing until window corner x is clicked
tu.done()


