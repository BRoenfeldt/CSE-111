import tkinter as tk
import os


# Define the function to change a single file name
def change_single_file_name(old_filename, new_filename):
    """Rename a file.
    Parameter old_filename: the current name of the file.
    Parameter new_filename: the new name for the file.
    """
    
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

def change_mutiple_file_names(directory, old_text, new_text):
    """Rename all files in a directory that contain old_text.
    Parameter directory: the directory containing the files.
    Parameter old_text: the text to replace in the file names.
    Parameter new_text: the text to replace old_text.
    """
    #try to rename the files and catch errors
    try:
        with open("name_changes.txt", "w") as file:
            for filename in os.listdir(directory):
                if old_text in filename:
                    new_filename = filename.replace(old_text, new_text)
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
    root.title("Simple GUI")
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

    # Create and pack the single file button
    single_file_button = tk.Button(root, text="Change Single File Name", command=lambda: change_single_file_name(user_file_old, user_file_new))
    single_file_button.pack()

    # Create and pack the multi file button
    multiple_file_button = tk.Button(root, text="Change Multiple File Names", command=lambda: change_mutiple_file_names(directory, user_file_old, user_file_new))
    multiple_file_button.pack()

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()