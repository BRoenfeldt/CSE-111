#finds a file and changes the name
import os

def rename_file(original_path, new_name):
    """
    Renames a file from its original path to a new name in the same directory.

    Parameters:
    original_path (str): The current path of the file including its name and extension.
    new_name (str): The new name for the file including the extension.

    Returns:
    bool: True if the file was successfully renamed, False otherwise.
    """
    # Check if the original file exists
    if not os.path.isfile(original_path):
        print(f"The file {original_path} does not exist.")
        return False

    # Extract directory path
    directory = os.path.dirname(original_path)

    # Construct new file path
    new_path = os.path.join(directory, new_name)

    # Rename the file
    try:
        os.rename(original_path, new_path)
        print(f"File renamed to {new_path}")
        return True
    except OSError as e:
        print(f"Error: {e}")
        return False

# Example usage
original_file_path = "./testing folder/new_name.txt"
new_file_name = "test.txt"
rename_file(original_file_path, new_file_name)