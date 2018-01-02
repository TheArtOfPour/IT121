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
tk.resizable(0, 0)
# Make the window stay on top
tk.wm_attributes("-topmost", 1)
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

    def fly_E(self):
        self.canvas.move(self.id, 1, 0)

    def firePhaser(self, xpos, ypos, angle):
        print("fire %s" % angle)
        lineID = self.canvas.create_line(xpos, ypos, xpos + 500, ypos + 500, fill="red", width=5)
        return lineID


# Create an Enterprise instance of the Ship class
EnterpriseImage = PhotoImage(file="enterprise.gif")
Enterprise = Ship(canvas, EnterpriseImage, -1000, 10)

# Create a Falcon instance of the Ship class
FalconImage = PhotoImage(file="falcon.gif")
Falcon = Ship(canvas, FalconImage, 200, 600)

# Start with phasers off
phaserCount = 0

# Loop to animate
while True:

    # move the Falcon a little bit
    Falcon.fly_NE()
    # If the ship left the screen move it back to the start
    pos = Falcon.canvas.coords(Falcon.id)
    if pos[0] > 900:
        Falcon.canvas.move(Falcon.id, -750, +750)

        # move the Enterprise a little bit
    Enterprise.fly_E()

    # If the ship left the screen move it back to the start
    pos = Enterprise.canvas.coords(Enterprise.id)
    if pos[0] > 900:
        Enterprise.canvas.move(Enterprise.id, -1900, 0)

    # Every 200 pixels fire phasers
    if pos[0] % 200 == 0:
        phaserCount = 25

    # Delete the last phaser if needed
    if pos[0] % 200 > 0 and pos[0] % 200 < 26:
        try:
            Enterprise.canvas.delete(lineID)
        except:
            pass

    if phaserCount > 0:
        lineID = Enterprise.firePhaser(pos[0] + 774, pos[1] + 183, "SE")
        phaserCount -= 1

    # refresh the screen
    tk.update_idletasks()
    tk.update()

    # wait a little bit to control animation speed
    time.sleep(0.01)
