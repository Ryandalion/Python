# Program reads a file named numbers.txt and displays all its contents

def main():

    numberData = open('numbers.txt', 'r'); # numberData variable will open the input file titled numbers.txt which holds a series of numbers and read from it

    numberOne = numberData.readline(); # numberOne is assigned to the first line in the text file

    while numberOne != '': # Loop while the line is not empty
        print(int(numberOne)); # Convert numberOne from string to float then print
        numberOne = numberData.readline(); # Assign numberOne to next line

    numberData.close(); # After exit from while loop we close the  numberData file

main(); # Execute main