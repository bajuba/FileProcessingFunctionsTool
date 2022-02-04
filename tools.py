#file variable used in menuFunction and chooseFile
filename = ""

#Chooses which file to change, creates empty file if file does not exist
#Option 1
def chooseFile():
    global filename
    filename = input("\nWhat file would you like to change?\n")
    my_file = open(filename, "a")
    my_file.close()
    return filename

#Removes every other character from a text file
#Option 8
def removeEveryOtherChar(filename):
    with open(filename, mode='r+') as f:
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

#Search a file for a string
# Option 17
def searchStr(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        phrase = input("\nEnter a phrase to see if it is contained within the file.\n")
        if phrase in content:
            print(f"\nYour phrase '{phrase}' is contained within file {filename}.\n")
        else:
            print(f"\nFile {filename} does not contain '{phrase}'.\n")
        f.close()
            