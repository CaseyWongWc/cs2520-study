def showme(path):
    with open(path, 'r') as file:
        contents = file.read()
        print(contents)
