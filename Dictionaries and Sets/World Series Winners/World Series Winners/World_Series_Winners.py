# Program gathers data from a text file (worldserieswinners.txt) and stores the data into a dictionary. There will be two dictionaries where one dictionary will have team name's as a key and the year as the other key

def main():
    inputFile = open("WorldSeriesWinners.txt","r");
    dataFile = inputFile.readlines();
    inputFile.close();
    numYears = len(dataFile); # Number of elements is equal to number of years because each team listed represents the winner of that year
   
    listYear = []; # List to hold the years of the World Series from 1903-2009 *excluding 1904 and 1994
    count = 0; # Counter variable
    startYear = 1903; # First year World Series was played
    while count < numYears: # Loop while count is less than numYears (length of the data)
        listYear.append(startYear + count); # Append each year to the list. The year starts from 1903 up until 2009
        count += 1; # Increment count by one

    listYear.remove(1904); # World Series was not played in 1904
    listYear.remove(1994); # World Series was not played in 1994

    # Team Dictionary - KEY: Team Name | VALUE: Number of World Series Wins
    count = 0;
    while count < len(dataFile): # Loop while count is less than the length of the data file
        dataFile[count] = dataFile[count].rstrip('\n'); # Remove the newline characters from each element inside the list
        count += 1; # Increment count by one
        
    teamDict = dict(); # Intiailize a dictionary for team. KEY: Team Names | VALUE: Number of Wins per team
    yearDict = dict(zip(listYear, dataFile)); # Create a dictionary for year. Initialize it by zipping the listYear and dataFile lists

    for dataFile in dataFile: # Loop through the data file list
        if dataFile in teamDict: # If the data file element exists in the dictionary we add one to it's existing value
            teamDict[dataFile] += 1;
        else: # If the data file element does not exist we initialize it's value to one
            teamDict[dataFile] = 1;

    userInput = 0; # Variable responsible for user's menu selection
    while userInput != 3: # Loop while the user has not chosen to exit
        print("\n1. Look up World Series Win by Year"); # Look up wins by year
        print("2. Look up World Series Win by Team"); # Look up wins by team
        print("3. Exit Program"); # Exit program
        userInput = int(input()); # Get the user input and convert it to an integer

        if userInput == 1: # If user selects 1, we execute lookupYear (look up wins for the year)
            lookupYear(yearDict);
        elif userInput == 2: # If user selects 2, we execute lookupTeam (look up wins by the team)
            lookupTeam(teamDict);

def lookupYear(yearDict): # Look up wins for the year
    userInput = int(input("\nEnter the year you would like to look up: ")); # Get user input for the year they want to find the winner for
    if userInput not in yearDict: # If the year does not exist in the dictionary we execute
        print("Data for the year",userInput,"is not available");
    else: # Else the year exists in the dcitionary and we print the value that corresponds to the key (user year)
        print(yearDict.get(userInput));

def lookupTeam(teamDict): # Look up wins by team
    userInput = input("\nEnter the team name you would like to look up: "); # Get the team name the user wants to look up
    if userInput not in teamDict: # Team name does not exist in dictionary because they have no wins or the user input a team name which we dont have data for (database only has data for 1904-2009)
        print("The team either has no wins or the data for the year is not available");
    else: # Team name exists and they have a win so we retrieve the value for the key and print
        print(teamDict.get(userInput), "wins");

print("World Series Winners Database (1903-2009)");
main(); # Execute main