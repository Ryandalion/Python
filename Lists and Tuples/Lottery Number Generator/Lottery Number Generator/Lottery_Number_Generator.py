# Program will generate a seven digit lottery number. Each number will be an element in a list and will be in the range of 0 to 9

import random; # Import random module to be used for generating a random number
import time; # Import the time module to use the sleep function

numGenerate = 7; # Constant numGenerate for the seven lucky numbers generated

def main():
    luckyNumbers = [0] * 7; # Initialize a list of 7 elements to zero
    index = 0; # Create an index counter and set it to zero

    while index < numGenerate: # Loop until index is no longer less than numGenerate (7)
        luckyNumbers[index] = random.randint(0,9); # Generate a random number between 0 and 9
        index += 1; # Increase index by one

    print("Lucky numbers have been generated");
    print("Please wait while we verify with the server");
    time.sleep(3); # Sleep for 3 seconds
    printLucky(luckyNumbers); # Call the printLucky function to print the list, pass the list as a parameter

def printLucky(luckyNumbers): # printLucky will print the list
    print("\nHere are the lucky numbers");
    print(luckyNumbers, end =" "); # Print until the end of the list
    print(); # Newline

print("Lucky Number Generator\n")
main();
