# Program will calculate the average of all the numbers inside the text file

def main():
    dataFile = open('numbers.txt', 'r'); # Open the text file that holds the numbers
    number = dataFile.readline(); # Assign the first line to number
    count = 0; # Variable to hold the number of elements inside the text file
    total = 0; # Variable that holds the sum of all elements in the text file

    while number != '': # Loop until empty
        total = total + int(number); # Add the number to the total. Convert the number from a string to a integer
        count += 1; # Increase the counter variable by one per loop
        number = dataFile.readline(); # Retrieve the next line and assign it to number
      
    dataFile.close(); # Close the file
    average = (total/count); # Calculate the average
    print(average); # Print the average

main();