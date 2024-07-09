import tkinter as tk
import os
"""
ADD IN THE FOLLOWING CODE TO THE MAIN.PY FILE
Add in better explanations, maybe another pop up window to show the user what the GUI is for.
Add in multiple file changes code to make it work
Think about testing files for final project
"""

def directory_fix(old_filename,directory):
    """Fix the directory path to be used in the change file name functions.
    Parameter directory: the directory path to fix.
    Returns: the fixed directory path.
    """
    # Remove leading and trailing whitespace
    directory = directory.strip()
    # Replace forward slashes with backslashes
    directory = directory.replace("\\", "/")
    edited_directory = "./" + directory + "/" + old_filename
    #print(f"Test directory: {directory}")
    return edited_directory

# Define the function to change a single file name
def change_single_file_name(old_directory, new_directory):
    """Rename a file.
    Parameter old_filename: the current name of the file.
    Parameter new_filename: the new name for the file.
    """
    #try to rename the file and catch errors
    try:
        os.rename(old_directory, new_directory)
        print(f"Successfully renamed '{old_directory}' to '{new_directory}'")
    except FileNotFoundError:
        print(f"Error: The file '{old_directory}' does not exist.")
    except FileExistsError:
        print(f"Error: The file '{old_directory}' already exists.")
    except PermissionError:
        print("Error: You don't have permission to rename this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#define the main function
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Change File Names")
    root.geometry("300x300")
    # Create and pack the header label
    header = tk.Label(root, text="Welcome to the File Name Change GUI!")
    header.pack(pady=10)
    #Explanation of the GUI
    explanation = tk.Label(root, text="Enter the file name you would like to change and the new file name. Then select the file or directory you would like to change. If a file contains the old file name, it will be changed to the new file name.", wraplength=250)
    explanation.pack(pady=20)

    # Create and pack the old file name entry
    old_file_entry = tk.Entry(root, width=30)
    old_file_entry.insert(0, "New File Name")
    old_file_entry.pack()
    # Create and pack the new file name entry
    new_file_entry = tk.Entry(root, width=30)
    new_file_entry.insert(0, "Old File Name")
    new_file_entry.pack()
    # Create and pack the directory entry
    directory_entry = tk.Entry(root, width=30)
    directory_entry.insert(0, "Directory")
    directory_entry.pack()

    #define the function to grab the inputs
    def grab_inputs():
        """Get the user inputs from the text fields.
        Returns: old_filename, new_filename, directory
        """
        old_filename = old_file_entry.get()
        new_filename = new_file_entry.get()
        directory = directory_entry.get()
        new_directory = directory_fix(old_filename, directory)
        old_directory = directory_fix(new_filename, directory)
        return new_directory, old_directory

    #define the function to execute the change single file name function
    def execute_change_single_file_name():
        """Get the user inputs and call the change_single_file_name function."""
        new_directory, old_directory = grab_inputs()
        #print(f"Old File Name: {old_filename}")
        #print(f"New File Name: {new_filename}")
        #print(f"Directory: {directory}")
        change_single_file_name(old_directory, new_directory)

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