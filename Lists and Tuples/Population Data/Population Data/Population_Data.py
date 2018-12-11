
# Program analyzes population data for the United States between the years 1950 - 1990. The program calculates the average annual change in population, the year with the greatest in crease, and the year with the lowest increase

YEARS = 40; # Constant is 40 because the data is from the year 1950 - 1990

def main():
    inputFile = open('USPopulation.txt','r'); # Open the text file containing the population data
    popData = inputFile.readlines(); # Copy the contents of the text file into the list 
    inputFile.close(); # Close file object

    count = 0;
    while count < YEARS: # Loop until count exceeds YEARS (50)
        popData[count] = popData[count].rstrip('\n'); # Remove the invisible newline character  
        popData[count] = int(popData[count]); # Convert the data from string to integer
        count += 1; # Increment count by one per loop iteration

    count = 0; # Re-intialize count to zero 
    yearFirst = 0; # Variable is for year 1
    yearSecond = 0; # Variable is for year 2 
    difference = 0; # Difference is year 2 - year 1 per loop iteration
    averageList = [0] * YEARS; # Create a list of 40 elements initialized to zero

    while count < YEARS: # Loop until count is greater than YEARS (40)
        yearFirst = popData[count]; # Set yearFirst to count
        yearSecond = popData[count+1]; # Set yearTwo to count + 1, the element after the firstYear
        difference = int(yearSecond) - int(yearFirst); # Subtract the two years to get the difference
        averageList[count] = difference; # Store the difference between the two years in a the averageList list
        count += 1; # Increment count by one

    count = 0; # Re-initialize count to zero
    greatest = averageList[0]; # Set the variable greatest to averageList[0]. This variable will be used for greater than comparison
    lowest = averageList[0]; # Set the variable lowest to averageList[0]. This variable will be used for lower than comparison
    greatestYear = 1950; # Set both greatest and lowest year to 1950 since that is the start date of the data
    lowestYear = 1950;

    while count < YEARS: # Loop until count is greater than 40
        if averageList[count] > greatest: # If the element inside averageList[count] is greater than the current greatest number we change the greater than to the new element
            greatest = averageList[count]; # Assign the element to the new greatest variable
            count += 1; # Increment counter variable by 1

        elif averageList[count] < lowest: # If the element at index is less than the lowest variable then we reassign the lowest variable
            lowest = averageList[count]; # We assign the lowest variable to the new element
            count += 1;

        else: # If there is no newest greater or lowest then we just increment count by one
            count += 1;

    greatestYear += (averageList.index(greatest) + 1); # We find the index value that holds the greatest element and add one (index counting) and assign it to greatest year (1950)
    lowestYear += (averageList.index(lowest) + 1); # We find the index value that holds the lowest element and add one and assign it to the lowest year (1950).
    
    print("The average change in the population over the time period was",(sum(averageList)/YEARS)); # To get the average, we take the list of differences between years and divide it by 40
    print("The year with the greatest population change was", greatestYear); # Print the greatest year which is 1950 + index value of greatest element
    print("The year with the lowest population change was", lowestYear); # Print the lowest year which is 1950 + index value of lowest element

print("United States Population Data - 1950's to 1990's\n");
main();