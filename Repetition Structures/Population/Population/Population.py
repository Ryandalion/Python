# Function that calculates the population of an organism given the starting number of organisms, daily increase percentage, and number of days given to multiply

numOrganisms = int(input("Enter the starting number of organisms: "));
while(numOrganisms < 0):
        print("Value cannot be negative");
        numOrganisms = int(input("Enter the starting number of organisms: "));

increaseRate = int(input("Enter the daily increase rate in percent: "));
while(increaseRate < 0):
        print("Value cannot be negative");
        increaseRate = int(input("Enter the daily increase rate in percent: "));

numDays = int(input("Enter the number of days you wish to calculate population growth: "));
while(numDays < 0):
        print("Value cannot be negative");
        numDays = int(input("Enter the number of days you wish to calculate population growth: "));

increaseRate = (increaseRate/100);
print();
print("Day Approximate ------------- Population");
print("1                               ", numOrganisms);
for x in range(2, numDays+1, 1):
    numOrganisms += (numOrganisms * increaseRate);
    print(x , "                              ", numOrganisms);

