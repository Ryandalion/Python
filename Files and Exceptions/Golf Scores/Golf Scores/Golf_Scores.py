# Program is designed for a golf course. The program will retrieve the user's name and their score and write it to a file named golf.txt. The program will also open the golf.txt file and display its contents

def main():
    running = 'y'; # Set a bool variable to y, this controls the while loop that determines if the user wants to enter another player's information
    outputFile = open('golf.txt', 'w'); # Create a file title golf.txt to record the player's name and score
    
    while running != 'n': # Loop while the user has not chosen n to exit
        userName = input("Enter the player's name: "); # Get player's name
        userScore = int(input("Enter the user's score: ")); # Get player's score
        outputFile.write(userName + '\n'); # Write the player's name to the text file
        outputFile.write(str(userScore) + '\n'); # Write the player's score to the text file
        running = input("Press y to enter another user or press n to exit: "); # User will either choose to continue or exit the program
        
    outputFile.close(); # Close the output file
    printGolf(); # Print the information from the file by calling the printGolf function

def printGolf(): # Print the information from the golf.txt file
    print("\nGolf Scores\n");
    inputFile = open('golf.txt','r'); # Open golf.txt file in read only mode
    currentLine = str(inputFile.readline()); # Convert the line to a string
    currentLine = currentLine.rstrip('\n'); # Remove the newline character

    while currentLine != '':
        print("Player Name: ", currentLine); # Print the player's name
        currentLine = str(inputFile.readline()); # Assign currentLine to the next line 
        print("Player Score: ", currentLine); # Print the player's score
        currentLine = str(inputFile.readline()); # Assign currentLine to the next line - Player's name
        currentLine = currentLine.rstrip('\n'); # Remove the newline character

    inputFile.close(); # Close the input file

main(); # Call main