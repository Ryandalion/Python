
#Function that keeps a running total of the number of bugs the user catches in a one week period

print("Day 1");
numBugs = int(input("Please input the number of bugs caught: "));

while(numBugs < 0):
    print("Number of bugs cannot be negative or zero");
    numBugs = int(input("Please input the number of bugs caught on day 1: "));
total = 0;
total += numBugs;

for x in range(0,6,1):
    print();
    print("Day", x + 2);
    numBugs = int(input("Please enter the number of bugs caught: "));
    while(numBugs < 0):
        print("The number of bugs cannot be negative or zero");
        numBugs = int(input("Please enter the number of bugs caught: "));
    total += numBugs;

print("The total number of bugs collected over a week period are", total);