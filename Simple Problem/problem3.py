#Write a python program to print the contents of a directory using the os module.Search online for the function which does that.
import os

# Specify the directory (or use the current directory)
directory = "D:\C++"  # "." refers to the current directory
try:
    # List the contents of the directory
    contents = os.listdir(directory)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access the directory '{directory}'.")
