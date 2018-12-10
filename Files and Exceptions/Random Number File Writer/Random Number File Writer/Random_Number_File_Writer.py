# Program will write random numbers to a file. The random numbers can range anywhere from 1 to 500. The user will set the amount of random numbers that should be generated and written to the file.

import random;

def main():
    
    numGenerate = int(input("Enter the number of random integers you would like to generate and write to the file: ")); # Retrieve the number of random numbers the user wishes to generate
    dataFile = open('random.txt', 'w'); # Create a random.txt file for writing data
    count = 0; # Variable to keep coutn

    for count in range(1,numGenerate+1): # Loop 1 to the number input by user (numGenerate)
        randomNum = random.randint(1,500); # Use random to generate a random number between 1 and 500
        dataFile.write(str(randomNum) + '\n'); # Write the random number to the random.txt fiel

    dataFile.close(); # Close the txt file
    print("Data has been written to random.txt");

main();
    