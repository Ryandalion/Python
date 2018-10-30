# Function that calculates the average and total rainfall. The program will ask the user for the number of years of data they wish to enter.

numYears = int(input("Please enter the number of years you wish to enter rainfall data for: "));
while(numYears < 0):
    numYears = int(input("The number of years cannot be negative. Please enter the number of years you wish to enter rainfall data for: "));
totalRain = 0;
avgRain = 0;
rainStat = 0;

for x in range(1,numYears+1, 1):
    for(y) in range(1,13,1):
        rainStat = int(input("Please enter the amount of rain for month " + str(y) + ":"));
        while(rainStat < 0):
            rainStat = int(input("Rain amount cannot be negative. Please enter the amount of rain for month " + str(y) + ":"));
        totalRain += rainStat;
    print("The total rain fall for year", x,"is", totalRain);
    print("The average rainfall per month is", format((totalRain/12), '.2f') + " inches");
    totalRain = 0;

