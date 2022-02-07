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

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""
        f.write(lyrics)
        f.close()

#Remove every character except abc and spcae from file
#Option 11
def abcSpace(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        whitelist = set('abc ABC')
        updated = ''.join(filter(whitelist.__contains__, content))
        f.truncate(0)
        f.write(updated)
        f.close

