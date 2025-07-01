import os 

folders = os.listdir("data")

for folder in folders:
    
    print(folder)
    print(os.listdir(f"data/{folder}"))


import os

# Ask user to enter the filename to search
search_file = input("Enter the file name to search: ")

# List all folders inside 'data'
folders = os.listdir("data")

found = False  # flag to check if file is found

# Loop through each folder inside 'data'
for folder in folders:
    # List files in each folder
    files = os.listdir(f"data/{folder}")
    
    # Check if the search file is in the current folder
    if search_file in files:
        print(f"File '{search_file}' found in folder: data/{folder}")
        found = True

if not found:
    print(f"File '{search_file}' not found in any folder.")
