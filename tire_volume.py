"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

import math



width = float(input("What is the width of the tire in mm? "))
ratio = float(input("What is the aspect ratio of the tire? "))
diam = float(input("What is the diameter of the tire in inches? "))
vol = (math.pi*(width*width)*ratio*(width*ratio+2540*diam)/10000000000)
print(f"The approximate volume of the tires is {vol:.2f} liters")