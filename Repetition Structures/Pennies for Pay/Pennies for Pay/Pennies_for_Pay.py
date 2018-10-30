# Function asks the user to enter a number of days to determine the number of pennies they would receive each day if the pennies multiplied by two per passing day

numDays = int(input("Enter the number of days you wish to calculate: "));
while(numDays < 0):
    numDays = int(input("Number of days cannot be zero. Please enter the number of days you wish to calculate: "));

numPennies = 1;
print("On day 1 you received", numPennies,"penny");

for x in range(1,numDays, 1):
    numPennies *= 2;
    print("On day " + str(x + 1) + " you recieved", numPennies, "pennies");

