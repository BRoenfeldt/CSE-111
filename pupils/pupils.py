import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    # Read the data from the pupils.csv file into a compound list.
    compound_list = read_compound_list("pupils.csv")
    # Print the compound list to the console.
    print_list(compound_list)
    #create lambda function to sort the compound list by birthdate
    birthdates_from_list = lambda list: list[BIRTHDATE_INDEX]
    #sort the birthdates in ascending order
    birthdates_print = sorted(compound_list, key=birthdates_from_list)
    #print(f"{birthdates_print}\n") print the birthdates in the order they are in the csv file
    #print the birthdates in ascending order
    print(f"Ordered from oldest to youngest\n{birthdates_print}")



def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(compound_list):
    """Print the compound list to the console.

    Parameter
        compound_list: the compound list to print.
    """
    for row in compound_list:
        print(f"{row}\n")


if __name__ == "__main__":
    main()