# Print hello five times

print("Print hello five times.")
for x in range(0, 5):
    print("Hello.")

# Count up
print("\nCount up.")
for x in range(0, 5):
    print("%s" % x)

# Count up slowly
print("\nCount up slowly.")
import time

for x in range(0, 5):
    time.sleep(1)
    print("%s" % x)

# Count down slowly
print("\nCount down slowly.")
for x in reversed(range(0, 5)):
    time.sleep(1)
    print("%s" % x)

# Loop through a list
kaiju = ['Godzilla', 'Mothra', 'Rhodan', 'Gamera']

print("\nRun... it's ", end="")
for x in kaiju:
    time.sleep(1)
    print("%s! " % x, end="")
print("Aaaaiiiii!\n\n")

# Complex countdown
for x in reversed(range(1, 100)):
    print("%s bottles of beer on the wall." % x)
    time.sleep(2)
    print("%s bottles of beeeeer." % x)
    time.sleep(2)
    print("Take one down,")
    time.sleep(1)
    print("pass it around.")
    time.sleep(1)
    print("%s bottles of beer on the wall." % (int(x) - 1))
    time.sleep(2)

# Nested loop for counting dance steps
print("\n\nDance steps:")
for x in range(1, 4):
    print("\n%s " % x, end="")
    time.sleep(0.5)
    for y in range(2, 4):
        print("%s " % y, end="")
        time.sleep(0.5)

# Math in a loop, doubling a penny for a month
print("\n\nDoubling a penny for a month:")
amount = 1
for x in range(1, 31):
    print("Day %s is %s dollars" % (x, amount / 100))
    amount = amount * 2
    time.sleep(1)

# sounds bark.wavView in a new window
import winsound

count = int(input("How many barks?"))

for x in range(0, count):
    winsound.PlaySound("bark.wav", 0)