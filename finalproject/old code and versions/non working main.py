import tkinter as tk
import os
"""
ADD IN THE FOLLOWING CODE TO THE MAIN.PY FILE
GRAB USER INPUTS FROM THE TEXT FIELDS TO BE USED IN THE CHANGE FILE NAME FUNCTIONS
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
    directory += "./" + directory + "/" + old_filename
    #print(f"Test directory: {directory}")
    return directory

# Define the function to change a single file name
def change_single_file_name(old_filename, new_filename, directory):
    """Rename a file.
    Parameter old_filename: the current name of the file.
    Parameter new_filename: the new name for the file.
    """
    directory = directory_fix(old_filename, directory)
    #try to rename the file and catch errors
    try:
        os.rename(old_filename, new_filename)
        print(f"Successfully renamed '{old_filename}' to '{new_filename}'")
    except FileNotFoundError:
        print(f"Error: The file '{old_filename}' does not exist.")
    except FileExistsError:
        print(f"Error: The file '{new_filename}' already exists.")
    except PermissionError:
        print("Error: You don't have permission to rename this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#define the function to change multiple file names
def change_mutiple_file_names(old_filename, new_filename, directory):
    """Rename all files in a directory that contain old_filename.
    Parameter directory: the directory containing the files.
    Parameter old_filename: the text to replace in the file names.
    Parameter new_filename: the text to replace old_filename.
    """
    #try to rename the files and catch errors
    try:
        with open("name_changes.txt", "w") as file:
            for filename in os.listdir(directory):
                if old_filename in filename:
                    new_filename = filename.replace(old_filename, new_filename)
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                    file.append(f"Renamed '{filename}' to '{new_filename}'\n")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to rename files in this directory.")
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
    explanation = tk.Label(root, text="Enter the file name you would like to change and the new file name. Then select the file or directory you would like to change. If a file contains any part of the old file name, it will be changed to the new file name.", wraplength=250)
    explanation.pack(pady=20)

    # Create and pack the old file name entry
    old_file_entry = tk.Entry(root, width=30)
    old_file_entry.insert(0, "Old File Name")
    old_file_entry.pack()
    # Create and pack the new file name entry
    new_file_entry = tk.Entry(root, width=30)
    new_file_entry.insert(0, "New File Name")
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
        return old_filename, new_filename, directory

    #define the function to execute the change single file name function
    def execute_change_single_file_name():
        """Get the user inputs and call the change_single_file_name function."""
        old_filename, new_filename, directory = grab_inputs()
        #print(f"Old File Name: {old_filename}")
        #print(f"New File Name: {new_filename}")
        #print(f"Directory: {directory}")
        change_single_file_name(old_filename, new_filename, directory)

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