
# Program searches for a name between two data sets. the first data set is 200 popular boy's names and the second set is 200 popular girl's names. Program will ask user to enter a name and it will search through the data and see if there is a match

NUM_NAMES = 200; # Create a constant of 200 for the 200 names in each text file

def main():
    inputFile = open('BoyNames.txt','r'); # Open the BoyNames.txt file in read only mode. The text file contains 200 boy's names that were popular between 2000 - 2009
    boyNames = inputFile.readlines(); # Copy all contents of text file into a list
    inputFile.close(); # Close the file object

    inputFile = open('GirlNames.txt','r'); # Open the GirlNames.txt file that contains the 200 most popular girl's names between the years 2000 - 2009
    girlNames = inputFile.readlines(); # Copy all contents to a list
    inputFile.close(); # Close the file object

    count = 0; # Create a counter variable and intiailize it to zero
    while count < NUM_NAMES: # Loop 200 times
        boyNames[count] = boyNames[count].rstrip('\n'); # Strip off invisible newline characters in the two lists
        girlNames[count] = girlNames[count].rstrip('\n');
        count += 1; # Increment count by one

    searchAgain = 'y'; # Create a bool variable that is used to control the while loop
    while searchAgain != 'n': # Loop until the user enters 'n'
        userSearch = input("Pleaes enter a name: "); # Get the name the user wants

        if userSearch in boyNames: # Search for the user specified name in the boy's names list
            print("The name", userSearch,"has been found in most popular Boy's names"); # If name exists, tell user that name exists
        elif userSearch in girlNames: # Search for the user specified name in the girl's names list
            print("The name", userSearch,"has been found in most popular Girl's names"); # If name exists, tell user that name exists
        else: # No name was found in both lists
            print("Name was not found"); # Inform user the name was not found

        searchAgain = input("\nWould you like to search another name? Enter Y to continue or N to exit: "); # Ask user if they want to search another name
        searchAgain.lower(); # Lower the user's input to lowercase

print("Popular Baby Names Database\n");
main(); # Execute main


