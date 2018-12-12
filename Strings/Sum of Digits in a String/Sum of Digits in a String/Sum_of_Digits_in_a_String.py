# Program asks user to enter a series of numbers as a string that are not separated. The program will then separate the numbers and calculate the sum.

def main():
    userNum = input("Please enter a series of numbers you wish to calculate the sum for (Enter numbers as one long string that are not separated by commas or whitespaces): "); # Retrieve user input string
    sum = 0; # Variable sum will hold the total of all numbers
    
    for x in userNum: # Loop x in user input number
        sum += int(x); # Convert the element at index x into a integer and add it to the sum variable

    print(sum); # Print the sum

main(); # Execute main