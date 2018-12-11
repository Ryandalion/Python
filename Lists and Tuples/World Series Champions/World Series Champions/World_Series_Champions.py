# Program determines the numbers of World Series of Baseball Championships that the user-specified team has won. The data for the program is a text file that contains a list of all World Series winners from 1903 - 2009.

WINNERS = 104; # There are 106 winners between the year 1903 - 2009. However, World Series was not played in 1904 and 1994

def main():
    inputFile = open('WorldSeriesWinners.txt','r'); # Open the World Series text file in read only mode
    worldSeries = inputFile.readlines(); # Transfer the contents of the text file into a list
    inputFile.close(); # Close the file object

    count = 0;
    while count < WINNERS: # Loop until count is greater than WINNERS (104)
        worldSeries[count] = worldSeries[count].rstrip('\n'); # Remove the invisible newline character
        count += 1; # Increment count by one

    searchAgain = 'y'; # Bool variable to control while loop
    while searchAgain == 'y': # Loop until user enters a character/integer other than 'y' 
        userSearch = input("Please enter the team you wish to find the number of World Series wins for: "); # Get the team name the user is looking for
        count = 0; # Counter variable
        numWins = 0; # Variable to hold the number of championships for the user specified team

        while count < WINNERS: # Loop until count is greater than WINNERS (104)
            if userSearch == worldSeries[count]: # If the user's team is found in the list we increment number of wins by 1 and increment count
                numWins += 1;
                count += 1;
            else: # No wins are found and we increment count to sift through the list
                count +=1;
                
        if numWins > 0: # If the user's team has at least one win then we print the message indicating the number of wins the team has
            print("The team", userSearch,"has won a total of",numWins,"World Series Championships");
        else: # Else if the team has no wins then we notify user
            print("The team", userSearch,"has no World Series Championships");

        searchAgain = input("\nWould you like to look up another team? Press Y to continue or N to exit: "); # Ask user if they want to search for another team
        searchAgain.lower(); # Lower any input from user
        print(); # Newline print

print("World Series of Baseball Championships Database (1903 - 2009)\n");
main(); # Execute main