import csv

PRODUCT_KEY_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    #store the products in a dictionary
    products_dict = read_dictionary('products.csv', PRODUCT_KEY_INDEX)
    #print the dictionary
    print(products_dict)
    print("\nRequested Items:")
    with open("request.csv") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            product_number = row[0]
            quantity = row[1]
            if product_number in products_dict:
                product_data = products_dict[product_number]
                product_name = product_data[PRODUCT_NAME_INDEX]
                product_price = float(product_data[PRODUCT_PRICE_INDEX])
                total_price = product_price * int(quantity)
                print(f"{quantity} {product_name} @ {product_price} = {total_price}")


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
    return data

if __name__ == '__main__':
    main()