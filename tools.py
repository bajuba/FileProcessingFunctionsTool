def removeEveryOtherChar():
    f = open("a")
    content = f.read()
    i = 0
    contentUpdated = ""
    for char in content:
        if char.isalpha() or char.isnumeric():
            if (i % 2) == 0:
                contentUpdated += char
            i += 1 
        else:
            contentUpdated += char
    print(contentUpdated)


removeEveryOtherChar()
