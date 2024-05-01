"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

from datetime import datetime

dayOfWeek = ""
def discountApplier(subtotal):
    if subtotal >= 50:
        subtotal = discountApplier(subtotal, dayChecker())
        print(f"Congratulations! You get a 10% discount.")
        subtotal = subtotal - subtotal*.1
        print(f"Your new subtotal is ${subtotal:.2f}")
    else:
        print(f"Sorry, no discount today.")
        print(f"Your subtotal is ${subtotal:.2f}")

def dayChecker(subtotal):
    weekInt = datetime.now().weekday()
    if weekInt == 0:
        dayOfWeek = "Monday"
        discountApplier(subtotal)
    elif weekInt == 1:
        dayOfWeek = "Tuesday"
        discountApplier(subtotal)
    elif weekInt == 2:
        dayOfWeek = "Wednesday"
        discountApplier(subtotal)
    elif weekInt == 3:
        dayOfWeek = "Thursday"
        discountApplier(subtotal)
    elif weekInt == 4:
        dayOfWeek = "Friday"
        discountApplier(subtotal)
    elif weekInt == 5:
        dayOfWeek = "Saturday"
        discountApplier(subtotal)
    elif weekInt == 6:
        dayOfWeek = "Sunday"
        discountApplier(subtotal)
    print(dayOfWeek)

    
    
subtotal = float(input("What is your subtotal?  $"))
dayChecker(subtotal)
