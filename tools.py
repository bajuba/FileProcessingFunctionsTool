import os
#Chooses which file to change, creates empty file if file does not exist
#Option 1
def chooseFile():
    file = input("\nWhat file would you like to change?\n")
    my_file = open(file, "a")
    my_file.close()
    return file

#Capitalize all letters in file
#Option 3
def capitalizeAllLetters(filename):
    with open(filename, mode='r+') as f:
       content = f.read()
       f.truncate(0)
       f.seek(0)
       contentUpdated = content.upper()
       f.write(contentUpdated)
       f.close
        
        
        

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

#Copy file
#Option 23
def copyFile(filename):
    with open(filename, 'r') as file:
        try:
            os.system('cls')#Clear console Windows
        except:
            os.system('clear')#Clear console Linux
        filename2 = filename + "_new"
        file2 = open(filename2, "w")
        file2 = file
        file.close()
        file2.close()
        print(f'The file "{filename}" was copied and the new file is called "{filename2}".')