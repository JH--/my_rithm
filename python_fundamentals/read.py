with open('first.txt', 'r') as file:
    data = file.read()
    print(data)

with open('first.txt', 'r+') as file:
    file.write("\nI'm at the beginnning\n")
    file.seek(100)
    file.write("\nI'm in the middle\n")
    file.seek(0)
    print(file.read())

with open('first.txt', 'a+') as file:
    file.write("\nI'm at the end\n")
    file.seek(0)
    print(file.read())

with open('first.txt', 'w+') as file:
    file.write("Now everything is overwritten :(")
    file.seek(0)
    print(file.read())
