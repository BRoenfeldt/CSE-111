import tkinter as tk
import os
"""
ADD IN THE FOLLOWING CODE TO THE MAIN.PY FILE
GRAB USER INPUTS FROM THE TEXT FIELDS TO BE USED IN THE CHANGE FILE NAME FUNCTIONS
"""

# Define the function to change a single file name
def change_single_file_name(new_filename, directory):
    """
    Renames a file from its original path to a new name in the same directory.

    Parameters:
    original_path (str): The current path of the file including its name and extension.
    new_name (str): The new name for the file including the extension.

    Returns:
    bool: True if the file was successfully renamed, False otherwise.
    """
    # Check if the original file exists
    if not os.path.isfile(directory):
        print(f"The file {directory} does not exist.")
    
    # Extract directory path
    directory = os.path.dirname(directory)

    # Construct new file path
    new_path = os.path.join(directory, new_filename)
    print(f"New path = {new_path}")
    # Rename the file
    try:
        os.rename(directory, new_path)
        print(f"File renamed to {new_path}")
    except OSError as e:
        print(f"Error: {e}")

#define the main function
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Change File Names")
    root.geometry("350x350")
    # Create and pack the header label
    header = tk.Label(root, text="Welcome to the File Name Change GUI!")
    header.pack(pady=10)
    #Explanation of the GUI
    explanation = tk.Label(root, text="Enter the file name you would like to change and the new file name. Then select the file or directory you would like to change. If a file contains any part of the old file name, it will be changed to the new file name.", wraplength=250)
    explanation.pack(pady=20)

    # Create and pack the new file name entry
    new_file_entry = tk.Entry(root, width=50)
    new_file_entry.insert(0, "New File Name including extension")
    new_file_entry.pack()
    # Create and pack the directory entry
    directory_entry = tk.Entry(root, width=50)
    directory_entry.insert(0, "Path to file, including file name and extension")
    directory_entry.pack()

    #define the function to grab the inputs
    def grab_inputs():
        """Get the user inputs from the text fields.
        Returns: new_filename, directory
        """
        new_filename = new_file_entry.get()
        directory = directory_entry.get()
        return new_filename, directory

    #define the function to execute the change single file name function
    def execute_change_single_file_name():
        """Get the user inputs and call the change_single_file_name function."""
        new_filename, directory = grab_inputs()
        #print(f"New File Name: {new_filename}")
        #print(f"Directory: {directory}")
        change_single_file_name(new_filename, directory)

    # Create and pack the single file button
    single_file_button = tk.Button(root, text="Change Single File Name", command=execute_change_single_file_name)
    single_file_button.pack()

    # Create and pack the multi file button
    multiple_file_button = tk.Button(root, text="Change Multiple File Names", command=execute_change_single_file_name)
    multiple_file_button.pack()

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()