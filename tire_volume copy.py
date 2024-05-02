"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

import math
from datetime import datetime


def computeVolume(width, ratio, diam):
    vol = (math.pi*(width*width)*ratio*(width*ratio+2540*diam)/10000000000)
    vol = round(vol, 2)
    print(f"The approximate volume of the tires is {vol:.2f} liters")
    return(width, ratio, diam, vol)

def  addToVolText():
    with open("tireVolume.txt", "a") as file:
        currentDateTime = datetime.now(tz=None)
        currentDateTime = currentDateTime.strftime("%m/%d/%Y")
        file.write(f"Date: {currentDateTime}, Tire Information: {getInputs()}, \n")


def getInputs():
    user_width = int(input("What is the width of the tire in mm? "))
    user_ratio = int(input("What is the aspect ratio of the tire? "))
    user_diam = int(input("What is the diameter of the tire in inches? "))
    commputeVolume(user_width, user_ratio, user_diam)
    if user_width >= 0 and user_ratio >= 0 and user_diam >= 0:
        print("test1.")
    elif user_width < 0 or user_ratio < 0 or user_diam < 0:
        print("test2.")
    elif user_width < 0 and user_ratio < 0 and user_diam < 0:
        print("test3.")
    else:
        print("test4.")



addToVolText()


