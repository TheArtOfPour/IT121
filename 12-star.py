# Preload game canvas
# Import Tk GUI interface module, tkinter
from tkinter import *
# Import time module to control animation speed
import time
# Create a Tk window object
tk = Tk()
# Set the window title attribute
tk.title("StarGame")
# Turn off window resizing
tk.resizable(0,0)
# Make the window stay on top
tk.wm_attributes("-topmost",1)
# Create a Canvas object for the window where we can start drawing
canvas = Canvas(tk, width=900, height=700, bd=0, bg="black", highlightthickness=0)
# Resize the borders to the canvas size
canvas.pack()
# Initialize for animation (?)
tk.update()

# Create a Ship class
class Ship:
    def __init__(self, canvas, myImage, xpos, ypos):
        self.canvas = canvas
        self.id = canvas.create_image(xpos, ypos, anchor=NW, image=myImage)

    # Define a method that flys East Northeast on the canvas 
    def fly_NE(self):
        self.canvas.move(self.id, 1, -1)



# Create a Falcon instance of the Ship class
myImage = PhotoImage(file="falcon.gif")
Falcon = Ship(canvas, myImage, 200, 600)

#Loop to animate
while True:
    #move the Falcon a little bit
    Falcon.fly_NE()

    #refresh the screen
    tk.update_idletasks()
    tk.update()

    #wait a little bit to control animation speed
    time.sleep(0.01)
