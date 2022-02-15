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
        f.close


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
    f.write(content_updated)
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