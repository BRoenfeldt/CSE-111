"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""
"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""


import math
"""
h = float(input("What is the length of the pendulum: "))
t = (2*math.pi)*math.sqrt(h/9.81)
print(f"It takes your pendulum {t:.2f} seconds to swing back and forth once.")

#function version

def pendulumTime():
    h = float(input("What is the length of the pendulum: "))
    t = (2*math.pi)*math.sqrt(h/9.81)
    print(f"It takes your pendulum {t:.2f} seconds to swing back and forth once.")

pendulumTime()

#function version2
"""
def pendulumTime(h):
    t = (2*math.pi)*math.sqrt(h/9.81)
    print(f"It takes your pendulum {t:.2f} seconds to swing back and forth once.")

h = float(input("What is the length of the pendulum? (in meters): "))
pendulumTime(h)