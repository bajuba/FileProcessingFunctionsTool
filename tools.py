
import os
from math import floor
import random

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
        
#Remove all instances of the word 'the' from file
#Option 5
def removeThe(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        contentUpdated = content.replace("the", "")
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

#Replace all for a specific string
#Option 19
def replaceString(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        phrase = input("\nEnter a phrase to see if it is contained within the file.\n")
        if phrase in content:
            f.truncate(0)
            f.seek(0)
            replacement = input("\nEnter what you would like to replace the phrase with.\n")
            contentUpdated = content.replace(phrase, replacement)
            f.write(contentUpdated)
            print(f"You have replaced {phrase} with {replacement}.\n")
        else:
            print("This string was not found in the file.")
            f.seek(0)


#Replace all
#Option 22
def replaceAll(filename):
    with open(filename, 'w') as f:
        replace = input("Enter what you would like to replace this text with: \n")
        f.write(replace)
#Removes all spaces from a text file
#Option 4
def removeSpaces(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.replace(' ','') for line in lines]
    with open(filename, 'w') as f:
        f.writelines(lines)
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

# Doubles every contiguous number (2 or more int in a row, not same numbers)
# Also Camel Casing for py?
# Option 13
def double_contiguous_numbers(filename):
  with open(filename,'r+') as f:
    file_raw = f.read()
    f.truncate(0)
    f.seek(0)
    content_updated = ""
    digit_temp = ""
    for char in file_raw:
      if char.isdigit():
        digit_temp += char
      elif char.isdigit() == False:
        if digit_temp != "" and len(digit_temp)>1:
          digit_temp = int(digit_temp) * 2
          content_updated += str(digit_temp)
        elif digit_temp != "" and len(digit_temp)==1:
          content_updated += str(digit_temp)
        digit_temp = ""
        content_updated += str(char)
    f.write(content_updated)
    f.close

#Search a file for a string
#Option 17
def searchStr(filename):
    with open(filename, mode='r') as f:
        content = f.read()
        phrase = input("\nEnter a phrase to see if it is contained within the file.\n")
        if phrase in content:
            print(f"\nYour phrase '{phrase}' is contained within file {filename}.\n")
            return True
        else:
            print(f"\nFile {filename} does not contain '{phrase}'.\n")
            return False

#Make file into two files
#Option 25
def splitFile(filename):
    contentNew = ""
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        num = floor(len(content) / 2)
        contentNew = content[num:len(content)]
        contentUpdated = content[0:num]
        f.write(contentUpdated)
    newFile = open(genRandomName(), "a")
    newFile.write(contentNew)

#Generate Random File Name
def genRandomName():
    newName = ""
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in range(8):
        rand = random.randrange(0, 25)
        cha = arr[rand]
        newName += cha
    return newName
