# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
#import csv to be used
import csv

#Set global variables for the product indexs
PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2


# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()


def main():
    #try to run the program and catch the errors
    try:
        #print store name
        print("Braden's Ballin Emporium\n")
        #store the products in a dictionary
        products_dict = read_dictionary('products.csv', PRODUCT_KEY_INDEX)
        #set the subtotal price to 0
        subtotal_price = 0
        #print the requested items
        print("\nRequested Items:")
        #open the request file and go thorugh it to get the requested items
        with open("request.csv") as file:
            reader = csv.reader(file)
            #skip the header row
            reader.__next__()
            for row in reader:
                #get the product number and quantity
                product_number = row[0]
                quantity = row[1]
                #set the product number and quantity to variables
                product_data = products_dict[product_number]
                product_name = product_data[PRODUCT_NAME_INDEX]
                product_price = float(product_data[PRODUCT_PRICE_INDEX])
                #set the item price to the product price times the quantity
                item_price = product_price * int(quantity)
                #iterate subtotal price by adding the item price
                subtotal_price += item_price
                #print the price per item and totals for each  item
                print(f"{quantity} {product_name} @ {product_price} = {item_price}")
        #print the subtotal, tax, and total  and  thabks
        print(f"\nSubtotal: ${subtotal_price:.2f}")
        print(f"Tax: ${subtotal_price * 0.06:.2f}")
        print(f"Total: ${subtotal_price * 1.06:.2f}")
        print(f"\nThank you for shopping at Braden's Ballin Emporium!\n {current_date_and_time:%A %I:%M %p}")
    #catch the errors for missing or wrongly named file
    except FileNotFoundError:
        print("Error: item request file is not found.")
    #catch the error for wrong product numbers
    except KeyError:
        print("Error: product number not found in products file.")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary to hold the data.
    data = {}
    # Open the file for reading.
    with open(filename, "r") as file:
        # Create a CSV reader object.
        reader = csv.reader(file)
        #skip the header row
        reader.__next__()
        # Iterate over the rows in the CSV file.
        for row in reader:
            # Get the key for the dictionary.
            key = row[key_column_index]
            # Store the row in the dictionary.
            data[key] = row
    #print the dictionary
    print(data)
    return data

# Call the main() function to run the program.
if __name__ == '__main__':
    main()