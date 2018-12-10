# Program will ask the user to enter 20 numbers. These numbers will be placed into a list and the average, sum, lowest, and highest number in the list will be calculated using built-in list functions

TOTAL_NUM = 20; # Constant of 20 to allow user to enter only 20 numbers

def main():
    numberData = [0] * TOTAL_NUM; # Intialize a list of 20 elements to zero
    index = 0; # Create a index variable to use as a counter

    while index < TOTAL_NUM: # Loop while index is less than TOTAL_NUM (20)
        userNum = int(input("Enter a number: ")); # Get user number
        numberData[index] = userNum; # Replace the element at index with user number
        index += 1; # Increase the index by one

    totalSum = sum(numberData); # Calculate sum
    average = totalSum / TOTAL_NUM; # Calculate average
    lowestNum = min(numberData); # Calculate minimum
    highNum = max(numberData); # Calculate maximum

    print("\nHere are the results"); # Print the results
    print("Total Sum: ", totalSum);
    print("Average: ", average);
    print("Lowest Number: ", lowestNum);
    print("Highest Number: ", highNum);

print("Number Analysis\n");
main(); # Execute main
