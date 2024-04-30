"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

import math
def boxCalculcator() :
    items = int(input("How many items do you have: "))
    itemsPerBox = int(input("How many items will you put in each box: "))
    boxes = math.ceil(items/itemsPerBox)
    print(f"You will need {boxes} boxes to store all of your items.")



boxCalculcator()
