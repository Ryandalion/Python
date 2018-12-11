# Program generates a list via random generation and compares it to a user input number n which will determine if the elements within the last are greater than the number

import random; # Import the random module to generate a random integer

def main():
    randNum = [0] * 10; # Intialize list with 10 elements of zero

    for x in range(10): # Loop 10 times
        randNum[x] = random.randint(0,10); # Generate a random number between 0 and 10
        x+=1; # Increment x by one

    userNum = int(input("Please enter a number: ")); # Get the user's number they wish to compare to the elements of the list

    print(randNum); # Print list for verification purposes
    numGreater = compareNum(randNum, userNum); # Send the list and the user number to the numGreater function to be evaluated
    print("There are",numGreater,"numbers greater than",userNum); # Print the results that were returned by the compare function

def compareNum(userList, userNum): # Function will compare the elements in the list to the user specified number. It will calculate the number of elements that are greater than the user number
    numGreater = 0; # Create a numGreater variable to hold the number of elements that are greater than the user specified number
    for x in range(len(userList)): # Loop through the length of the list
        if userNum < userList[x]: # If list element is greater than user number execute
            numGreater += 1; # Increase the numGreater variable by one
            x += 1; # Increase the counter variable
        else: # If userNum is greater than the list element
            x +=1; # Increase x by one
    return numGreater; # Return the results to the caller

print("Larger than N\n")
main(); # Execute main


        
