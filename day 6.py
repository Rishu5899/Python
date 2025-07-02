# Step 1: Open a file in write mode and write some text
with open("example.txt", "w") as file:
    file.write("Hello, this is a file I/O example.\n")
    file.write("We are writing and then reading from a file.")

# Step 2: Open the same file in read mode and print the content
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n")
    print(content)
