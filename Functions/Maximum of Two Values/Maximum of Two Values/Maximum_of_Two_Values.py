# Function that determines greatest number out of two numbers

def compareNum(num1, num2): # Function determines which number is the biggest between the two parameters
    if(num1 > num2): # If number 1 is greater than number 2, then number 1 is the greatest number
        greatestNum = num1;
        lowestNum = num2;

    else: # If number 2 is greater than number 1, then number 2 
        greatestNum = num2;
        lowestNum = num1;

    return greatestNum; # Return the number that is greatest
 
def main(): # Function gathers the user input
    num1 = int(input("Enter the first number: "));
    num2 = int(input("Enter the second number: "));
    greatestNum = compareNum(num1, num2); # Pass num1 and num2 to be compared and assign the return value from compareNum to greatestNum. greatestNum will be equal the the greatest number between num1 and num2
    print("The greatest number is", greatestNum); # Display the greatest num to the user

print("Which number is greatest?");
print();
main(); # Call main to begin execution of main functions