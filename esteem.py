"""
Braden Roenfeldt
Brother Keers
12:45
"""


def main():

    #prints the introduction to the program
    print(f"This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.")

    #initialize score as 0
    score = 0
    #Set each questsion as a variable so it can be passed to the question functions
    q1 = "  1. I feel that I am a person of worth, at least on an equal plane with others."
    q2 = "  2. I feel that I have a number of good qualities."
    q3 = "  3. All in all, I am inclined to feel that I am a failure."
    q4 = "  4. I am able to do things as well as most other people."
    q5 = "  5. I feel I do not have much to be proud of."
    q6 = "  6. I take a positive attitude toward myself."
    q7 = "  7. On the whole, I am satisfied with myself."
    q8 = "  8. I wish I could have more respect for myself."
    q9 = "  9. I certainly feel useless at times."
    q10 = " 10. At times I think I am no good at all."

    #loops through questions 1-5 calling the  function to sent the questions to the user and get the answer then calling the getScore function to get the score of the answer
    for question in [q1, q2, q3, q4, q5]:
        answer = questions1_10(question)
        score += getScorePos(answer)
        #loops through questions 6-10 calling the  function to sent the questions to the user and get the answer then calling the getScore function to get the score of the answer
    for question in [q6, q7, q8, q9, q10]:
        answer = questions1_10(question)
        score += getScoreNeg(answer)
    #prints the score and the interpretation of the score
    print(f"\nYour score is {score}.\nA score below 15 may indicate problematic low self-esteem.")


def questions1_10(question):
    """
    Function to ask questions 1-5
    Parameters:
        question: string to be asked to the user
    Returns: 
        answer: string of the user's response
    """
    #asks the user the question and gets the answer to return the answer
    answer = input(f"{question} Answer (D, d, a, A): ")
    #print(answer)
    return answer

def getScorePos(answer):
    """
    Function to get the score of the user's response for questions 1-5
    Parameters:
        answer: string of the user's response
    Returns: 
        score: int of the user's score
    """
    #if the answer is D the score is 0
    if answer == "D":
        score = 0
    #if the answer is d the score is 1
    elif answer == "d":
        score = 1
    #if the answer is a the score is 2
    elif answer == "a":
        score = 2
    #if the answer is A the score is 3
    elif answer == "A":
        score = 3
    return score

def getScoreNeg(answer):
    """
    Function to get the score of the user's response for questions 6-10
    Parameters:
        answer: string of the user's response
    Returns: 
        score: int of the user's score
    """
    #if the answer is D the score is 3
    if answer == "D":
        score = 3
    #if the answer is d the score is 2
    elif answer == "d":
        score = 2
    #if the answer is a the score is 1
    elif answer == "a":
        score = 1
    #if the answer is A the score is 0
    elif answer == "A":
        score = 0
    return score

#runs main function
if __name__ == "__main__":
    main()