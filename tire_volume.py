"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

import math
from datetime import datetime

def computeVolume():
    width = int(input("What is the width of the tire in mm? "))
    ratio = int(input("What is the aspect ratio of the tire? "))
    diam = int(input("What is the diameter of the tire in inches? "))
    vol = (math.pi*(width*width)*ratio*(width*ratio+2540*diam)/10000000000)
    vol = round(vol, 2)
    return(width, ratio, diam, vol)
    #print(f"The approximate volume of the tires is {vol:.2f} liters")

def  addToVolText():
    with open("tireVolume.txt", "a") as file:
        currentDateTime = datetime.now(tz=None)
        currentDateTime = currentDateTime.strftime("%m/%d/%Y")
        file.write(f"Date: {currentDateTime}, Tire Information: {computeVolume()}\n")
        #print(currentDateTime)

addToVolText()