"""Braden Roenfeldt
Brother Keers
CSE111 -  12:45
"""

from datetime import datetime

def discountApplier(subtotal):
    if subtotal >= 50:
        print(f"Congratulations! You get a 10% discount.")
        oldSubtotal = subtotal
        subtotal = subtotal - subtotal*.1
        print(f"Your new subtotal is ${subtotal:.2f}")
        print(f"Your discount amount is ${oldSubtotal-subtotal:.2f}")
        tax(subtotal)
    else:
        print(f"Sorry, no discount today.")
        print(f"Your subtotal is ${subtotal:.2f}")
        tax(subtotal)

def discountDenier(subtotal):
        print(f"Sorry, no discount today.")
        print(f"Your subtotal is ${subtotal:.2f}")
        tax(subtotal)

def dayChecker(subtotal):
    weekInt = datetime.now().weekday()
    if weekInt == 0:
        dayOfWeek = "Monday"
        discountDenier(subtotal)
    elif weekInt == 1:
        dayOfWeek = "Tuesday"
        discountApplier(subtotal)
    elif weekInt == 2:
        dayOfWeek = "Wednesday"
        discountApplier(subtotal)
    elif weekInt == 3:
        dayOfWeek = "Thursday"
        discountDenier(subtotal)
    elif weekInt == 4:
        dayOfWeek = "Friday"
        discountDenier(subtotal)
    elif weekInt == 5:
        dayOfWeek = "Saturday"
        discountDenier(subtotal)
    elif weekInt == 6:
        dayOfWeek = "Sunday"
        disscountDenier(subtotal)
    #print(dayOfWeek)

def tax(subtotal):
    tax_rate = 0.06
    tax = subtotal * tax_rate
    print(f"Your tax is ${tax:.2f}")
    total = subtotal + tax
    print(f"Your total is ${total:.2f}")
    
user_subtotal = float(input("What is your subtotal?  $"))
dayChecker(user_subtotal)
