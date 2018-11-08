# Program is a simple rock paper scissors game versus the computer. The computer's hand will be randomly generated and the user will input theirs. Then the program will determine the winner. If it is a tie, a rematch will execute

import random; # Import random module to use randint

def generate_random(): # Generate a random number that corresponds to either rock,paper, or scissors
    randNum = random.randint(1,3);
    return randNum; # Return the generated number to caller

def calculate_winner(userHand, computerHand): # Function calculates the winner between computer and user
    if(userHand == 1 and computerHand == 3):
        print("User Wins");
    elif(userHand == 2 and computerHand == 1):
        print("User Wins");
    elif(userHand == 3 and computerHand == 2):
        print("User Wins");
    elif(userHand == 3 and computerHand == 1):
        print("Computer Wins");
    elif(userHand == 1 and computerHand == 2):
        print("Computer Wins");
    elif(userHand == 2 and computerHand == 3):
        print("Computer Wins");
    else: # If it is a draw then we set tie status to true and return to caller
        print("It is a tie");
        tieStatus = 0;
        return tieStatus;

def main(): # Function is responsible for getting user input and calling the appropriate functions and handling the while loop
    status = 1;
    while(status != -1): # Keep looping until status equals -1
        computerHand = generate_random(); # Generate a random number and assign it to computer hand
        print("Select your move");
        print("1. Rock");
        print("2. Paper");
        print("3. Scissors");
        userHand = int(input()); # Get user's selection
        status = calculate_winner(userHand, computerHand); # Send the user's and the computer's hand as arguments to the calculate_winner function
        if(status == 0): # If the return value from calculate_winner is 0, a tie has occured and we execute another round
            status = 1;
        else: # There was a winner and we assign status -1 to exit the while loop and program
            status = -1;

print("Rock, Paper, or Scissors");
print();
main();