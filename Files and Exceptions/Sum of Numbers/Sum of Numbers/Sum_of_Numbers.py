# Program reads a text file that contains a series of integers and adds them all up

def main():
    dataFile = open('numbers.txt', 'r'); # Open the file named numbers.txt in read only mode
    number = dataFile.readline(); # Read the first line of the text file
    total = 0; # total variable will hold the sum of all the numbers combined

    while number != '': # Loop until we reach the end of the file
        total = total + int(number); # Add the number to the total. Convert number from a string to integer via built-in int function
        number = dataFile.readline(); # Assign next line to number

    dataFile.close(); # Close data file
    print(total); # Print the total
main(); # Call main