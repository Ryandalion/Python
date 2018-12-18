
# Program will create a dictionary of all west coast US states and their capital and ask the user to guess the capital of the state they are shown. The program will keep track of incorrect and correct guesses

import random; # Import random module so we can execute the random.choice function

def main():
    westCoast = {}; # Create an empty dictionary to hold the key-value pairs of West Coast states and their capitals
    westCoast = {"Arizona":"Phoenix", "Colorado":"Denver","Idaho":"Boise","Montana":"Billings","Nevada":"Carson City","New Mexico":"Albuquerque","Utah":"Salt Lake City","Wyoming":"Cheyenne","Alaska":"Juneau","California":"Sacramento","Hawaii":"Honolulu","Oregon":"Salem","Washington":"Olympia"}
    userSelection = 0; # User selection will hold the user's menu selection
    numTries = 0; # numTries keeps track of the number of attempts the user makes to guess the correct capital

    while userSelection != 2: # Loop while user selection is not equal to 2
        print("Guess the capital!");
        print("1. Start game");
        print("2. Exit game");
        userSelection = int(input("Enter your selection: ")); # Get the user's selection and convert it to an integer so it can be used in an if statement
        print();
        if userSelection == 1: # If user selects 1, we execute the game and pass the numTries variable and the dictionary as arguments
            numTries = startGame(numTries, westCoast);

def startGame(numTries, userDictionary): # Start game function gets the number of tries and dictionary as parameters
    state = random.choice(list(userDictionary.keys())); # Generate a random key via the random.choice function
    capital = userDictionary.get(state); # Retrieve the value of the key and assign it to capital
    print("State: ",state); # Print the state's name that the user will guess the capital for
    userInput = input("Enter the capital: "); # Get the user's input for the capital
    if userInput == capital: # If the user's input for capital are equal then the user has gotten the capital right and we execute
        print("You are correct! The capital of",state,"is",capital,"!"); # Print the state's name and capital
        print("It took you",numTries,"tries!"); # Print the number of tries it took the usre
        numTries = 0; # Reset number of tries in case the user wants to play again
        print();
        return numTries; # Return number of tries
    else: # user did not guess the correct answer and we execute
        print("Sorry that is incorrect");
        print();
        numTries += 1; # Increment number of tries by one
        return numTries; # Return number of tries

main(); # Execute main