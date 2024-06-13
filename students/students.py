"""
Braden Roenfeldt
Brother Keers
12:45
"""


def main():
    students = read_dictionary("students.csv")
    userInput = int(input("What is the I-Number you are looking for? "))
    length = len(students)
    counter = 0
    for key in students:
        counter += 1    #counter to keep track of how many times the loop has run      
        if userInput == int(key):
            print(students[key])
            break   #breaks the loop if the number is found
        elif counter == length:     #checks if the counter is equal to the length of the dictionary to determine if the number was not found
            print("I-Number not found")
    #print(counter)
    #print(length)
            


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "r") as file:
        students = {}
        skip_header = 1
        for line in file:
            if skip_header > 0:
                skip_header -= 1
                continue
            parts = line.split(",")
            students[parts[0]] = parts[1].strip()
            number = parts[0]
            name = parts[1]
        print(students)
    return(students)


"""
def read_dictionary(filename, key_column_index):
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    
"""





if __name__ == "__main__":
    main()