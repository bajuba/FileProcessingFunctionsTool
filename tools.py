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