"""
Braden Roenfeldt
Brother Keers
12:45
"""


def main():
    # Get an odometer value in U.S. miles from the user.
    userMilesStart = float(input("Enter the starting odometer value in miles: "))
    # Get another odometer value in U.S. miles from the user.
    userMilesEnd = float(input("Enter the ending odometer value in miles: "))
    # Get a fuel amount in U.S. gallons from the user.
    userGallons = float(input("Enter the amount of fuel in gallons: "))
    # Call the miles_per_gallon function and store the result in a variable named mpg.
    mpg = miles_per_gallon(userMilesStart, userMilesEnd, userGallons)
    # Call the lp100k_from_mpg function to convert the miles per gallon to liters per 100 kilometers and store the result in a variable named lp100k.
    lpg = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f"The fuel efficiency is {mpg:.2f} miles per gallon and {lpg:.2f} liters per 100 kilometers.")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles) / amount_gallons
    return(mpg)


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lpg = 235.215 / mpg
    return(lpg)


# Call the main function so that
# this program will start executing.
main()