import tools 

#Menu description
menuOptions = {
    1: "Choose a different file to change",
    2: "add input to file",
    3: "capitalize all letters in file",
    4: "remove spaces from file",
    5: "remove all instances of the word 'the' from file",
    6: "reverse the file",
    7: "double the file",
    8: "remove every other character from the file",
    9: "sum all numbers in the file",
    10: "replace every character in the file with it's ascii value",
    11: "remove every character except a,b,c and space from the file",
    12: "Capitalize every third letter in the file",
    13: "double every contiguous number in the file",
    14: "add ' ever since the incident' before each '.' in the file",
    15: "add random amounts of random characters randomly throughout the file",
    16: "alphabetize the file",
    17: "search the file for a string",
    18: "add a line return after each '.' in the file",
    19: "implement a replace all for a matched string in the file",
    20: "add rick astley lyrics to the file",
    21: "return the number of characters in the file",
    22: "implement a replace all",
    23: "make a copy of the file",
    24: "combine two files",
    25: "separate the file into two files",
    26: "add your own idea"
}

#Menu functionality: Call functions here
def menuUse(choice):
    #Use tools.filename to access the most recent filename
    while choice != "q":
        if choice == "1":
            tools.chooseFile()
        elif choice == "2":
            print("In Progress")
        elif choice == "3":
            tools.capitalizeAllLetters(tools.filename)
        elif choice == "4":
            tools.removeSpaces(filename)
        elif choice == "5":
            tools.removeThe(tools.filename)
        elif choice == "6":
            print("In Progress")
        elif choice == "7":
            print("In Progress")
        elif choice == "8":
            tools.removeEveryOtherChar(tools.filename)
        elif choice == "9":
            print("In Progress")
        elif choice == "10":
            print("In Progress")
        elif choice == "11":
            tools.abcSpace(filename)
        elif choice == "12":
            print("In Progress")
        elif choice == "13":
            tools.double_contiguous_numbers(tools.filename)
        elif choice == "14":
            print("In Progress")
        elif choice == "15":
            print("In Progress")
        elif choice == "16":
            print("In Progress")
        elif choice == "17":
            tools.searchStr(tools.filename)
        elif choice == "18":
            print("In Progress")
        elif choice == "19":
            print("In Progress")
        elif choice == "20":
            tools.rickAstley(filename)
        elif choice == "21":
            print("In Progress")
        elif choice == "22":
            print("In Progress")
        elif choice == "23":
            tools.copyFile(filename)
        elif choice == "24":
            print("In Progress")
        elif choice == "25":
            tools.splitFile(tools.filename)
        elif choice == "26":
            print("In Progress")
        elif choice == "q":
            print("I hope we solved your problem!")
            exit()
        else:
            print("Please enter a valid response.")
        input("Press enter to continue...")
        printMenu()
        choice = input("\nWhat would you like to do?\n")

#Prints all menu Options
def printMenu():
    #For each key value pair in the menuOptions dictionary, print it out
    for key in menuOptions.keys():
        print (key, '--', menuOptions[key] )
    print("Enter 'q' to quit." )

#Menu Start
def menu():
    print("\nChoose how you would like to use your files.")
    tools.chooseFile()
    printMenu()
    choice = input("\nWhat would you like to do?\n")
    menuUse(choice)
