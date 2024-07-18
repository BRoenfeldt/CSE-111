import tkinter as tk
import os
from datetime import datetime

#Link to usage example on Youtube: https://youtu.be/K0L0LbTjmBI


def directory_fix(old_filename, directory):
    """Fix the directory path to be used in the change file name functions.
    Parameter directory: the directory path to fix.
    Returns: the fixed directory path.
    """
    # Remove leading and trailing whitespace
    directory = directory.strip()
    # Replace forward slashes with backslashes
    directory = directory.replace("\\", "/")
    edited_directory = "./" + directory + "/" + old_filename
    #debeugging print
    print(f"Test directory: {edited_directory}")
    #return the edited/fixed directory
    return edited_directory

# Define the function to change a single file name
def change_single_file_name(old_directory, new_directory):
    """Rename a file.
    Parameter old_filename: the current name of the file.
    Parameter new_filename: the new name for the file.
    """
    #try to rename the file and catch errors
    try:
        #rename the file
        os.rename(old_directory, new_directory)
        #log the changes
        log_changes(old_directory, new_directory)
        #print success messasge
        print(f"Successfully renamed '{old_directory}' to '{new_directory}'. Check log.txt for more information.")
        return None
    #catch the errors and print out the error message
    except FileNotFoundError:
        print(f"Error: The file '{old_directory}' does not exist.")
    except FileExistsError:
        print(f"Error: The file '{old_directory}' already exists.")
    except PermissionError:
        print("Error: You don't have permission to rename this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def log_changes(old_directory, new_directory):
    """Log the changes made to the file names.
    Parameter old_filename: the current name of the file.
    Parameter new_filename: the new name for the file.
    """
    # Get the current date and time
    current_time = datetime.now(tz=None)
    current_time = current_time.strftime("%Y/%m/%d - %H:%M:%S")
    # Open the log file in append mode
    with open("change_log.txt", "a") as file:
        # Write the changes to the log file
        file.write(f"Change made: {old_directory} -> {new_directory} at {current_time}\n")
    return None

#define the main function
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Change File Names")
    root.geometry("550x250")
    # Create and pack the header label
    header = tk.Label(root, text="Welcome to the File Name Change GUI!")
    header.pack(pady=10)
    #Explanation of the GUI
    explanation = tk.Label(root, text="Enter the file name you would like to change and the new file name. Then select the file or directory you would like to change. If a file contains the old file name, it will be changed to the new file name.", wraplength=400)
    explanation.pack(pady=20)

    # Create and pack the old file name entry
    old_file_entry = tk.Entry(root, width=80)
    old_file_entry.insert(0, "New File Name - ex: CSE11_notes.txt")
    old_file_entry.pack()
    # Create and pack the new file name entry
    new_file_entry = tk.Entry(root, width=80)
    new_file_entry.insert(0, "Old File Name - ex: class_notes.txt")
    new_file_entry.pack()
    # Create and pack the directory entry
    directory_entry = tk.Entry(root, width=80)
    directory_entry.insert(0, "Directory - ex: myFiles/importantFiles (Must be in the same folder as where this script is ran)")
    directory_entry.pack()

    #define the function to grab the inputs
    def grab_inputs():
        """Get the user inputs from the text fields.
        Returns: old_filename, new_filename, directory
        """
        #Set the variables to the user inputs by grabbing the text from the entry fields
        old_filename = old_file_entry.get()
        new_filename = new_file_entry.get()
        directory = directory_entry.get()
        #call the directory fix function to fix the directory path using the new and old filenames
        new_directory = directory_fix(old_filename, directory)
        old_directory = directory_fix(new_filename, directory)
        #return  all the variables
        return new_directory, old_directory

    #define the function to execute the change single file name function
    def execute_change_single_file_name():
        """Get the user inputs and call the change_single_file_name function."""
        #set new_directory and old_directory to the return values of the grab_inputs function
        new_directory, old_directory = grab_inputs()
        #debugging prints
            #print(f"Old File Name: {old_filename}")
            #print(f"New File Name: {new_filename}")
            #print(f"Directory: {directory}")
        #call the change_single_file_name function with the new_directory and old_directory variables
        change_single_file_name(old_directory, new_directory)

    # Create and pack the single file button
    single_file_button = tk.Button(root, text="Change Single File Name", command=execute_change_single_file_name)
    single_file_button.pack()

    # Start the GUI event loop
    root.mainloop()

#run the main function if imported
if __name__ == "__main__":
    main()