"""
Braden Roenfeldt
Brother Keers
12:45
"""

questionCounter = 1
userInput = ""

def main():


    print(f"This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.")
    while userInput == "A" or "a" or "d" or "D":
        if questionCounter == 1:
            userInputCheck(question1(), questionCounter)
            print(userInput)
        elif questionCounter == 2:
            question2()
        elif questionCounter == 3:
            question3()
        elif questionCounter == 4:
            question4()
        elif questionCounter == 5:
            question5()
        elif questionCounter == 6:
            question6()
        elif questionCounter == 7:
            question7()
        elif questionCounter == 8:
            question8()
        elif questionCounter == 9:
            question9()
        elif questionCounter == 10:
            question10()
        questionCounter += 1
        


def  userInputCheck(Input, questionCounter):
    if Input != "A" or "a" or "d" or "D":
        print("Invalid input. Please enter A, a, D, or d.")
        questionCounter -= 1

def question1():
    userInput = input(f"I feel that I am a person of worth, at least on an equal plane with others. ")
    return (userInput)

def question2():
    userQ2 = input(f"I feel that I have a number of good qualities. ")

def question3():
    userQ3 = input(f"All in all, I am inclined to feel that I am a failure. ")

def question4():
    userQ4 = input(f"I am able to do things as well as most other people. ")

def question5():
    userQ5 = input(f"I feel I do not have much to be proud of. ")

def question6():
    userQ6 = input(f"I take a positive attitude toward myself. ")

def question7():
    userQ7 = input(f"On the whole, I am satisfied with myself. ")

def question8():
    userQ8 = input(f"I wish I could have more respect for myself. ")

def question9():
    userQ9 = input(f"I certainly feel useless at times. ")

def question10():
    userQ10 = input(f"At times I think I am no good at all. ")



#runs main function
if __name__ == "__main__":
    main()