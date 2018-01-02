import sys
#Print hello five times
print ("Print hello five times with a FOR loop.")
for x in range(0,5):
      print("Hello.")

print ("\nPrint hello five times with a WHILE loop.")
counter=0
while counter < 5:
        print("Hello.")
        counter = counter + 1
      

#Count up slowly
import time
print ("\nCount up slowly with a FOR loop.")
for x in range(0,5):
        time.sleep(1)
        print("%s" % x)

print ("\nCount up slowly with a WHILE loop.")
counter=0
while counter < 5:
        counter = counter + 1
        time.sleep(1)
        print("%s" % counter)
      

#Loop through a list
kaiju=['Godzilla','Mothra','Rhodan','Gamera']

print ("\nRun...  it's ", end="")
counter=0
while counter < len(kaiju):
        time.sleep(1)
        print("%s!  " % kaiju[counter], end="")
        counter = counter+1
        
print ("Aaaaiiiii!\n\n")


#Nested loop for counting dance steps
print ("\n\nDance steps:")
outerCounter=1
while outerCounter < 4:
        print ("\n%s " % outerCounter,end="")
        time.sleep(0.5)
        innerCounter = 2
        while innerCounter < 4:
                print ("%s " % innerCounter,end="")
                time.sleep(0.5)
                innerCounter = innerCounter + 1
        outerCounter = outerCounter + 1

#Math in a loop, doubling a penny for a month
print ("\n\nDoubling a penny for a month:")
amount=1
day = 1
while day < 31:
        print ("Day %s is %s dollars" % (day,amount/100))
        amount = amount * 2
        time.sleep(1)
        day = day + 1

#loop until break
while True:
        print("Keep going? (y to continue): ",end="")
        response=sys.stdin.readline()
        response=response.rstrip()
        if response == "y":
                print("OK, we'll keep going.")
                time.sleep(1)
                continue
        else:
                print("OK, we'll stop.")
                time.sleep(1)
                break
                
        print("This never prints.")

#bounce in a box
import random
import turtle
t=turtle.Pen()
t.shape("circle")
rightSide=100
leftSide=-100
topSide=100
bottomSide=-100

x,y=t.position()
while True:
        while (leftSide < x < rightSide) and (bottomSide < y < topSide):
                t.forward(5)
                x,y=t.position()
        print ("after while")
        print (t.position(),t.heading())
        if x >= 100:
                direction=random.randint(110,250)
                t.setheading(direction)
                t.forward(5)
                x,y=t.position()
                print ("after right")
                print (t.position(),t.heading())
        if x <= -100:
                direction=random.randint(290,430)
                t.setheading(direction)
                t.forward(5)
                x,y=t.position()
                print ("after left")
                print (t.position(),t.heading())
        if y <= -100:
                direction=random.randint(20,160)
                t.setheading(direction)
                heading=t.heading()
                t.forward(5)
                x,y=t.position()
                print ("after bottom")
                print (t.position(),t.heading())
        if y >= 100:
                direction=random.randint(200,340)
                t.setheading(direction)
                t.forward(5)
                x,y=t.position()
                print ("after top")
                print (t.position(),t.heading())
#        print ("Enter to continue:",end="")
#        temp=sys.stdin.readline()