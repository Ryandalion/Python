# Function that asks the user to enter a series of positive numbers and calculates the sum. The program exits the while loop when the user enters a negative number.

print("Enter a positive number or a negative number to calculate the sum");

sum = 0;
userNum = 0;

while(userNum >= 0):
    userNum = int(input("Please enter a number: "));
    if(userNum < 0):
        break;
    else:
        sum += userNum;
print("The sum of all numbers is", sum);