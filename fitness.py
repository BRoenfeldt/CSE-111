# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import sys


def main():
    # Get the user's gender, birthdate, height, and weight.
    userGender = input("Enter your gender (M/F): ")
    userGender = userGender.upper()     #Converts user input to uppercase for input checking
    if userGender != "M" and userGender != "F":    #Checks that user input is correct and exits if not
        print(f"Misinput data, exiting.")
        sys.exit()
    userInchHeight = float(input("Enter your height in inches: "))
    userPoundWeight = float(input("Enter your weight in pounds: "))
    userBirthday = input("Enter your birthdate (YYYY-MM-DD): ")
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index, and basal_metabolic_rate functions as needed.
    # Print the results for the user to see.
    userAge = compute_age(userBirthday)
    print(f"Age {userAge} (years).")
    userKiloWeight = kg_from_lb(userPoundWeight)
    print(f"Weight {userKiloWeight:.2f} (kg).")
    userCmHeight = cm_from_in(userInchHeight)
    print(f"Height {userCmHeight:.1f} (cm).")
    userBMI = body_mass_index(userKiloWeight, userCmHeight)
    print(f"Your BMI is {userBMI:.1f}.")
    userBMR = basal_metabolic_rate(userGender, userKiloWeight, userCmHeight, userAge)
    print(f"Your BMR is {userBMR:.0f} kcals/day.")
    pass

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    #Calculates and returns the mass in kilograms
    kilos = pounds * 0.45359237
    return kilos

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    #Calculates and returns the length in centimeters
    centimeters = inches * 2.54
    return centimeters

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    #Calculates and returns BMI
    bmi = (10000*weight) / (height**2)
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    #Checks the parameter again, exiting if incorrect, and calculates the BMR based on the Gender. Returns the BMR
    if gender == "M":
        bmr = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
    elif gender == "F":
        bmr = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)
    else:
        print(f"Misinput data, exiting.")
        sys.exit()
    return bmr

#Main function call
if __name__ == "__main__":
    main()