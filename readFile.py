f=open("file.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)