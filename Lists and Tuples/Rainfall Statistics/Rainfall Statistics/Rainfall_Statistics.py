# Program gathers rainfall data for 12 months. It will then calculate the average, total, highest, and lowest amount months

MONTHS = 12; # MONTHS is a constant set to 12 to represent the 12 months in a year

def main():
    rainfallData = [0] * MONTHS; # Intialize a list of 12 elements to zero
    index = 0; # Set index (counter) variable to zero
   
    while index < MONTHS: # Loop until index is no longer less than MONTHS (12)
        rain = int(input("Enter the rainfall data for month " + str(index + 1) + ": ")); # Get the rain data for the month
        rainfallData[index] = rain;
        rain = 0; # Set rain to zero to prepare it for the next input
        index +=1; # Increase index variable by one per loop iteration

    totalRain = totalRainfall(rainfallData); # Send the rainfallData as a parameter to calculate the total rainfall
    average = averageRain(rainfallData); # Send the rainfallData as a parameter to calculate the average rainfall
    minRain = min(rainfallData); # Use built-in list function MIN to find the minimum value in the list
    maxRain = max(rainfallData); # Use built-in list function MAX to find the maximum value in the list
    minMonth = rainfallData.index(minRain); # Find the index where the first instance of minRain occurs
    maxMonth = rainfallData.index(maxRain); # Find the index where the first instance of maxRain occurs
    minMonth += 1; # Increase minMonth and maxMonth by 1 to account for list indexing
    maxMonth += 1;
    print("\nRainfall Data Statistics\n"); # Print the rain data
    print("Average Rain: ", format(average, ',.2f')); 
    print("Total Rain: ", totalRain);
    print("Minimum Rain Month: ", minMonth);
    print("Maximum Rain Month: ", maxMonth);
    print();

def totalRainfall(rainData): # Function calculates the sum of the list
    totalRain = sum(rainData);
    return totalRain; # Returns the sum

def averageRain(rainData): # Function calculates the average of the list
    averageRain = (sum(rainData))/MONTHS;
    return averageRain; # Returns the average

print("Rainfall Database\n");
main(); # Execute main