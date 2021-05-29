###############################################################################
# Author: Karteikay Dhuper
# Date: May 4th 2021
# Description This program emulates a solo wheel of fortune game by having the
# player guess a censored phrase using vowels and consonant alphabets.
###############################################################################
import random as r  
import os
import time 

def get_phrase (): # returns a random phrase from phrase.txt file

    with open ('phrases.txt') as fo: #context manager created
        phrase_list = []
        for line in fo:
            phrase_list.append(line.rstrip()) # appends each line of the file to phrase_list

    random_phrase = r.choice(phrase_list)  # chooses a random element from list (uses .choice function from "random" module")
    return random_phrase

def get_censored_phrase(phrase): # this function takes the random phrase generated from previous function and censors it
    censoredPhraseList = []

    for char in phrase:
        if char.isalpha() == True: # if char in random_phrase is an alphabet convert it to "_"
            char = "_"
        elif char == " ": # if its a whitespace leave it as a whitespace
            char = " "
        elif char == "'": # keeps apostrophe same too
            char = "'"
        else: # if its anything else then leave it as a special character
            char = char
        censoredPhraseList.append(char) # list contains the characters from the random_phrase but censored with "_"

    #censoredPhrase = "".join(censoredPhraseList) # joins all elements of censored list without commas and brackets
    random_censored_phrase = str("".join(censoredPhraseList)) # converts it to string for return value
    return random_censored_phrase

def spin_the_wheel(unusedConsonants): # function spins a virtual wheel of money

    # initializes wheel
    virtualWheel = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT' ]

    if len(unusedConsonants) != 0: # makes sure the user has consonants to use
        wheelResult = r.choice(virtualWheel) # returns random value from virtualWheel list
    else:
        wheelResult = "There are no consonants left."

    return wheelResult

def main_menu_controls(): # function prints the list of controls for the player as a "user-interface" of sorts
   
    #––––––––––––––––––––––––––––––––––––––––
    return print("\nWhat would you like to do?"
    +"\n  1 - Spin the wheel"
    +"\n  2 - Buy a vowel"
    +"\n  3 - Solve the puzzle"
    +"\n  4 - Quit the game")
    
def consonants(phrase, correct_letters, unusedConsonants, usedConsonants, mutable_phrase, result, earnings,displayUnusedVow,displayEarnings, revealed_phrase, censoredPhrase): # handles the logic after the user spins the wheel
    isConsonant = False 
    pickedConsonant = input("Pick a consonant: ")
    # while loop makes sure a valid consonant is entered
    while isConsonant == False:
        if pickedConsonant in 'aeiou': # make sure letter is not a vowel
            print("Vowels must be purchased.")
            pickedConsonant = input("Pick a consonant: ")
        elif pickedConsonant.isdigit() == True: # makes sure its not a number
            print(f"The character {pickedConsonant} is not a letter.")
            pickedConsonant = input("Pick a consonant: ")
        elif len(pickedConsonant) > 1: # makes sure only one character is entered
            print("Please enter exactly one character.")
            pickedConsonant = input("Pick a consonant: ")
        else: # if provided letter is consonant then program proceeds to check if it is in the phrase
            isConsonant == True
            usedConsonants.append(pickedConsonant.upper())
            updatedConsonants = []

            for letter in unusedConsonants: # for loop coverts the used consonants to a "_" and stores it in "updatedConsonants" list                    
                if letter in usedConsonants:
                    letter = "_"
                else:
                    letter = letter
                updatedConsonants.append(letter)
            # unusedConsonants.remove(pickedConsonant.upper()) # removes the consonant from the unused constants list
            displayUpdatedConsanants = "".join(updatedConsonants)

            occurances = phrase.count(pickedConsonant) # checks if the provided consonant is in the phrase

            os.system('clear') # clears everything in the terminal before this command to make it seem like the gameboard is being updated

            if occurances > 0:
                correct_letters.append(pickedConsonant) # adds picked consonant to list of correct letters

                revealed_phrase.clear() # clears list before converting 
                for letter in mutable_phrase:
                    if letter in correct_letters:
                        letter = letter
                    elif letter.isalpha() == True: # if letter in mutable_phrase is an alphabet convert it to "_"
                        letter = "_"
                    elif letter == " ": # if its a whitespace leave it as a whitespace
                        letter = " "
                    elif letter == "'": # keeps apostrophe same too
                        letter = "'"
                    else: # if its anything else then leave it as a special character
                        letter = letter
                    revealed_phrase.append(letter)

            updated_phrase = "".join(revealed_phrase) # stores the elements of revealed_phrase list in joined string format for printing on game board 
                        
            # informs the player if they guessed a letter in the censored message
            if occurances == 1:
                print(f"There is 1 {pickedConsonant.upper()}," + f" which earns you ${result}.")
                earnings += result
                # Updates the game board –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                header = print("::::::::::::::::::::::::::::::::::::::::: Solo Wheel of Fortune ::")
                display_phrase = print(f"::{updated_phrase.center(62)}::")
                midder = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                heads_up_display = print(f"::  {displayUpdatedConsanants.center(29)} ::" + f" {displayUnusedVow.center(14)}::" + f"  {earnings} ::")
                footer = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                # Finishes updating the game board –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                break
            elif occurances > 1:
                print(f"There are {occurances}" + f" {pickedConsonant.upper()}'s," + f" which earns you ${result*occurances}")
                earnings += (result * occurances)
                # Updates the game board –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                header = print("::::::::::::::::::::::::::::::::::::::::: Solo Wheel of Fortune ::")
                display_phrase = print(f"::{updated_phrase.center(62)}::")
                midder = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                heads_up_display = print(f"::  {displayUpdatedConsanants.center(29)} ::" + f" {displayUnusedVow.center(14)}::" + f"  {earnings} ::")
                footer = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                # Finishes updating the game board –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                break
            else:
                print(f"I'm sorry, there are no {pickedConsonant.upper()}'s.")
                # Generates the game board ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                header = print("::::::::::::::::::::::::::::::::::::::::: Solo Wheel of Fortune ::")
                display_phrase = print(f"::{updated_phrase.center(62)}::")
                midder = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                heads_up_display = print(f"::  {displayUpdatedConsanants.center(29)} ::" + f" {displayUnusedVow.center(14)}::" + f"  {displayEarnings} ::")
                footer = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                # Finishes generating game board ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                break

def main():

    # Initializing the nessecary variables –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    phrase = get_phrase().lower() # gets uncensored phrase and stores it in "phrase" variable
    mutable_phrase = list(phrase) # makes it so that phrase can be mutated 
    censoredPhrase = get_censored_phrase(phrase) # converts phrase to censored phrase using function
    revealed_phrase = [] # stores phrase with guessed letters

    # dynamic lists that store unused letters
    unusedConsonants = ['B','C','D','F','G','H','J','K','L','M','N','P', 'Q','R','S','T','V','W','X','Y','Z']
    unusedVowels = ['A','E','I','O','U']
    
    # list stores the letters that were guessed correctly by player
    correct_letters = [] 
    # list stores consonants that have been played
    usedConsonants = []

    # list that is to be printed on the gameboard
    displayUnusedCons = "".join(unusedConsonants)
    displayUnusedVow = "".join(unusedVowels)

    earnings = 0
    displayEarnings = str(earnings).rjust(8)
    # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    os.system('clear') # clears everything in the terminal before this command
    print("*THE ANSWER IS* --> " + phrase)
    # Generates the game board ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    header = print("::::::::::::::::::::::::::::::::::::::::: Solo Wheel of Fortune ::")
    display_phrase = print(f"::{censoredPhrase.center(62)}::")
    midder = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    heads_up_display = print(f"::  {displayUnusedCons.center(29)} ::" + f" {displayUnusedVow.center(9)}::" + f"  {displayEarnings.rjust(13)} ::")
    footer = print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    # Finishes generating game board ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    # prints controls independant of "main_menu_controls" function to allow 1 second introduction on first run 
    print("\nWhat would you like to do?")
    time.sleep(1)
    print("  1 - Spin the wheel")
    time.sleep(1)
    print("  2 - Buy a vowel")
    time.sleep(1)
    print("  3 - Solve the puzzle")
    time.sleep(1)
    print("  4 - Quit the game") # prints controls on the console
    time.sleep(1)

    msg = "Enter the number of your choice: "
    userAction = input(msg)

    # ––––– Deals with the output of the wheel ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    
    while userAction != '4': # as long as the user's action is not 4 and is fully numeric following code will run
        
        if userAction == '1': # ––––– Logic for spinning the wheel –––––––––––––––––––
            result = spin_the_wheel(unusedConsonants)
            if result == 'BANKRUPT':
                earnings = 0
                result = int(0)
                #displayEarnings = str(0).rjust(8)
                #os.system('clear')
                print("The wheel landed on BANKRUPT")
                main_menu_controls()
                userAction = input(msg)

            elif result == "There are no consonants left.":
                print(result)
            
            elif result > 0:
                #earnings += result
                print(f"The wheel landed on ${result}.")
            
            else: "Error"
            consonants(phrase,correct_letters,unusedConsonants, usedConsonants, mutable_phrase,result,earnings, displayUnusedVow,displayEarnings, revealed_phrase,censoredPhrase) # runs the logic to determine if the player guessed a consonant
            time.sleep(1) # gives user time to evaluate before presenting menu
            
        elif userAction == '2': # –––– Logic for buying a vowel ––––––––––––––––––––––
            print("This action is still being worked on.")

        elif userAction == '3':  # ––– Logic for solving the puzzle ––––––––––––––––––
            if len(revealed_phrase) == 0:
                guess = input("Enter your solution: ")
            else:
                print(f"    Clues: {''.join(revealed_phrase)}")
                guess = input("    Guess: ")
            if guess == phrase:
                print("Ladies and gentlemen, we have a winner!")
                break
            else:
                print("I'm sorry, the correct solution was:")
                print(phrase.upper())
                break

        elif userAction == '4': # ––– Logic for quitting the game –––––––––––––––––––––
            break

        else:
            print("\nPlease choose a number between 1-4")
            time.sleep(1)

        time.sleep(0.1)
        print("\nWhat would you like to do?")
        time.sleep(0.1)
        print("  1 - Spin the wheel")
        time.sleep(0.1)
        print("  2 - Buy a vowel")
        time.sleep(0.1)
        print("  3 - Solve the puzzle")
        time.sleep(0.1)
        print("  4 - Quit the game") # prints controls on the console
        time.sleep(0.1)
        userAction = input(msg)
 
    print("Thanks for playing!")
    exit()
    
    # ––––– Deals with the output of the wheel ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

if __name__ == '__main__':
    main()
