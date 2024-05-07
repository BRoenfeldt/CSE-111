"""
Braden Roenfeldt
Brother Keers
12:45
"""

def main():
    #Get user gender, birthday, weight (lbs), height (in)
    userGender = input("Enter your gender (M or F): ")
    userBirthday = input("Enter your birthday (YYYY-MM-DD): ")
    userPoundWeight = float(input("Enter your weight in pounds: "))
    userInchHeight = float(input("Enter your height in inches: "))
    #Converts user weight to kilograms and height to centimeters
    userKiloWeight = kiloWeight(userPoundWeight)
    userCmHeight = cmHeight(userInchHeight)
    bmiCalc(userKiloWeight, userCmHeight)
    userAge = birthdayCalc(userBirthday)
    bmrCalc(userGender, userKiloWeight, userCmHeight, userAge)
    

def kiloWeight(poundWeight):
    """Converts pounds to kilograms
    Parameters
        poundWeight: A weight in pounds
    Returns: The converted weight in kilograms
    """
    kiloWeight = poundWeight * 0.45359237
    return kiloWeight

def cmHeight(inchHeight):
    """Converts inches to centimeters
    Parameters
        inchHeight: A height in inches
    Returns: The converted height in centimeters
    """
    cmHeight = inchHeight * 2.54
    return cmHeight

def bmiCalc(kiloWeight, cmHeight):
    """Calculates BMI
    Parameters
        kiloWeight: A weight in kilograms
        cmHeight: A height in centimeters
    Returns: The calculated BMI
    """
    bmi = kiloWeight / ((cmHeight/100) ** 2)
    print(f"Your BMI is {bmi:.2f}")
    return bmi

def bmrCalc(userGender, userKiloWeight, userCmHeight, userAge):
    """Calculates BMR
    Parameters
        userGender: The user's gender
        userKiloWeight: The user's weight in kilograms
        userCmHeight: The user's height in centimeters
        userAge: The user's age
    Returns: The calculated BMR
    """


main()