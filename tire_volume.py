"""
Author: Braden Roenfeldt
Professor: Brother Keers
URL: 

This file creates or appends to a text file named tireVolume.txt with the date and tire information taken from the user input from the terminal.
"""

import math
from datetime import datetime

def computeVolume():
    """
    Gets user input from terminal and calculates the volume of the tire

    Args:
        None

    Returns:
        3 integers: width, ratio, diameter
        1 float: volume
    """
    width = int(input("What is the width of the tire in mm? "))
    ratio = int(input("What is the aspect ratio of the tire? "))
    diam = int(input("What is the diameter of the tire in inches? "))
    vol = (math.pi*(width*width)*ratio*(width*ratio+2540*diam)/10000000000)
    vol = round(vol, 2)
    return(width, ratio, diam, vol)
    #print(f"The approximate volume of the tires is {vol:.2f} liters") used for debugging

def  addToVolText():
    """
    Adds the date and tire information to a text file named tireVolume.txt
    Calls computeVolume() to get the tire information

    Args:
        None

    Returns:
        None
    """
    with open("tireVolume.txt", "a") as file:
        currentDateTime = datetime.now(tz=None)
        currentDateTime = currentDateTime.strftime("%m/%d/%Y")
        file.write(f"Date: {currentDateTime}, Tire Information: {computeVolume()}\n")
        #print(currentDateTime), used for debugging

def main():
    addToVolText()

if __name__ == "__main__":
    main()