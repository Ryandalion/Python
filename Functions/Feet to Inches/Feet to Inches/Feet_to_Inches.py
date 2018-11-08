# Program that converts feet to inches

def feetInches(feet): # Function converts feet to inches
    inches = feet/12;
    return inches;

def main(): # Function that validates user input and calls the function to convert feet to inches
    inches = float(input("Enter the inches you wish to convert to feet: "));
    while(inches < 0):
        inches = float(input("Inches must be greater than zero. Enter the inches you wish to convert to feet: "));
    feet = feetInches(inches);
    print(inches,"inches converted is", format(feet,'.2f'),"feet"); # Display the inches to the user

print("Convert Inches to Feet");
print();
main(); # Call main function to execute all functions