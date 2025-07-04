
with open("ser.txt", "w") as file:
    file.write("Hello, my name is Rishu.\n")
    file.write("This is a File I/O example in Python.\n")


with open("ser.txt", "r") as file:
    content = file.read()
    print("File Content:\n")
    print(content)
