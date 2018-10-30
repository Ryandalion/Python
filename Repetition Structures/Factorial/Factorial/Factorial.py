# Function that calculates the factorial of a user input number

userNum = int(input("Please enter a number you wish to find the factorial for: "));
factorial = 1;
original = userNum;
for x in range(userNum, 0, -1):
    factorial *= x;

print("The factorial of ",original, ":", factorial);