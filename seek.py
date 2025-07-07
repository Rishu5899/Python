with open("te.txt","r") as f:
    print(type(f))
    f.seek(5)
    print(f.tell())
    data = f.read(10)
    print(data)