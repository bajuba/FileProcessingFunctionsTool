import tools
choice = 0

filename = input("Enter filename: ")
file = open(filename,'a')


print("1. choose file")
print("2. add input to file")
print("4. capitalize all letters in file")
print("5. remove spaces from file")
print("6. remove all instances of the word 'the' from file")
print("1. reverse the file")
print("1. double the file")
print("1. remove every other character from the file")
print("1. sum all numbers in the file")
print("1. replace every character in the file with it's ascii value")
print("1. remove every character except a,b,c and space from the file")
print("1. Capitalize every third letter in the file")
print("1. double every contiguous number in the file")
print("1. add ' ever since the incident' before each '.' in the file")
print("1. add random amounts of random characters randomly throughout the file")
print("alphabetize the file")
print("search the file for a string")
print("18. add a line return after each '.' in the file")
print("1. implement a replace all for a matched string in the file")
print("1. add rick astley lyrics to the file")
print("1. return the number of characters in the file")
print("1. implement a replace all")
print("23. make a copy of the file")
print("24. combine two files")
print("1. separate the file into two files")
print("26. add your own idea")

choice = int(input("Make a choice"))

if(choice == 1):
  file.close()
  filename = input("Enter filename: ")
  file = open(filename,'a')
if(choice == 2):
  file.write(input("add what?"))
  file.close()
  file = open(filename,'a')
