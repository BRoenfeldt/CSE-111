"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45"""



"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

user_age = int(input("Enter your age here: "))
max_rate = 220 - user_age
maxtarget_rate = max_rate*.85
mintarget_rate = max_rate*.65

print(f"Your target heart rate to get the most out of your excersize is between {mintarget_rate:.0f} and {maxtarget_rate:.0f} beats per minute.")