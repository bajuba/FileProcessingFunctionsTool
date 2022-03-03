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

#Removes all spaces from a text file
#Option 4
def removeSpaces(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.replace(' ','') for line in lines]
    with open(filename, 'w') as f:
        f.writelines(lines)
        f.close

# Remove all instances of the word 'the' from file
# Option 5
def remove_the(filename):
    with open(filename, mode='r+') as f:
        clear_console()
        content = f.read()
        f.truncate(0)
        f.seek(0)
        content_updated = content.replace("the", "")
        f.write(content_updated)

#Reverse the file
#Option 6
def reverseFile(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        contentUpdated = ""
        for line in reversed(content):
            contentUpdated += line
        f.write(contentUpdated)



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




#Replace every character in the file with it's ascii value
#Option 10
def replaceCharacterWithAscii(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        contentUpdated = ""
        for char in content:
            contentUpdated += str(ord(char)) + '\n'
        f.write(contentUpdated)
        f.close


# Capitalize every third letter in the file
# Option 12
def capitalize_every_third(filename):
  with open(filename,'r+') as f:
    file_raw = f.read()
    f.truncate(0)
    f.seek(0)
    content_updated = ""
    i = 0
    for char in file_raw:
      if char.isalpha():
        i += 1
        if i%3 == 0:
          char = char.capitalize()
          content_updated += str(char)
        else:
          content_updated += str(char)
      else:
        content_updated += str(char)
    f.write(content_updated)
    f.close


#Copy file
#Option 23
def copy_file(filename):
    with open(filename, 'r') as file:
        clear_console()
        filename_2 = filename + "_new"
        file_2 = open(filename_2, "w")
        file_2 = file
        file_2.close()
        print(f'The file "{filename}" was copied and the new file is called "{filename_2}".')


# Doubles every contiguous number (2 or more int in a row, not same numbers)
# Also Camel Casing for py?
# Doubles every number, contiguous numbers are doubled as one number
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
        if digit_temp != "":
          digit_temp = int(digit_temp) * 2
          content_updated += str(digit_temp)
        digit_temp = ""
        content_updated += str(char)
    if digit_temp != "":
      digit_temp = int(digit_temp) * 2
      content_updated += str(digit_temp)
    f.write(content_updated)
    f.close

# Add 'ever since the incident' before each '.' in file
# Option 14
def the_incident(filename):
    with open(filename, mode='r+') as f:
        clear_console()
        content = f.read()
        f.truncate(0)
        f.seek(0)
        content_updated = content.replace(".", " ever since the incident.")
        f.write(content_updated)

# Add random amounts of random characters throughout file randomly, number range can be tweaked
# Option 15
def add_random_char(filename):
  with open(filename,'r+') as f:
    file_raw = f.read()
    f.truncate(0)
    f.seek(0)
    content_updated = ''
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rand_char = ''
    for char in file_raw:
      rand_int = random.randrange(0,25)
      if rand_int == 10:
        content_updated += char
        rand_loop = random.randrange(1,10)
        for i in range(rand_loop):
          rand_loop_three = random.randrange(0,25)
          rand_char += arr[rand_loop_three]
          content_updated += rand_char
          rand_char = ''
      else:
        content_updated += char
    f.write(content_updated)
    f.close

# Alphabetizes file by line
# Option 16
def alphabetize_file(filename):
  with open(filename,'r+') as f:
    sorted_lines = list()
    for line in f:
      sorted_lines.append(line.strip())  
    sorted_lines.sort()
    f.truncate(0)
    f.seek(0)
    for item in sorted_lines:
      f.write(item + '\n')
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


#Add Rick Astley lyrics to file
#option 20
def rickAstley(filename):
    with open(filename, mode='a+') as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        lyrics = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""
        f.write(lyrics)
        f.close


#Replace all
#Option 22
def replaceAll(filename):
    with open(filename, 'w') as f:
        replace = input("Enter what you would like to replace this text with: \n")
        f.write(replace)


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


#Clear Console
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')