# Program is a random number guessing game. The program will generate a random number between 1 and 100 and ask the user to guess the number. If the user guesses correctly they are congratulated and if they do not guess correctly they can continue to guess

import random; # Import random module to use randint function

def generate_random(): # Function generates a random number between 1 and 100
    randNum = random.randint(1,100);
    return randNum; # Return the random number to the caller

def numGuesses(numGuess): # Function displays the number of guesses the user took to guess the correct answer
    print("Number of guesses: ", numGuess);

def main(): # Function responsible  for getting user input and calling the appropriate functions
    status = 1; # Sentinel for while loop
    numGuess = 0; # Collects the number of guesses the user takes
    randNum = generate_random(); # Generate a random number via the function and assign it to randNum
    while(status != -1): # Keep looping until the user enters -1
        userGuess = int(input("Enter your guess: ")); # Get user guess
        numGuess += 1; # Add one to the total number of guesses per loop iteration
        if(userGuess == randNum): # If the user's number matches the random number we execute
            print("Congratulations, you are correct!");
            numGuesses(numGuess); # Print the number of guesses the user took
            randNum = generate_random(); # Generate a new random number in case they want to play again
            print("Enter 1 to play again or -1 to exit");
            userChoice = int(input()); # Get user choice
            if(userChoice == -1): # If user enters -1 then we exit while loop
                status = -1;
              
        else: # User number is not equal to the random number
            print("Wrong guess");
            print("Try again?");
            print("Enter 1 to play again or -1 to exit"); # User can play again or exit
            userChoice = int(input());
            if(userChoice == -1): # User chooses to exit program
                status = -1; # Set status to -1 so we exit loop and program
                print("The number was", randNum); # Display the random number to the user

print("Random Number Guessing Game");
main();