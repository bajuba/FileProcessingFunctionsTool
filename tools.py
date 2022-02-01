#Option 8
def removeEveryOtherChar():
    file = input("What file would you like to remove every other character from?")
    with open(file, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        i = 0
        contentUpdated = ""
        for char in content:
            if char.isalpha() or char.isnumeric():
                if (i % 2) == 0:
                    contentUpdated += char
                i += 1 
            else:
                contentUpdated += char
        f.write(contentUpdated)
        f.close