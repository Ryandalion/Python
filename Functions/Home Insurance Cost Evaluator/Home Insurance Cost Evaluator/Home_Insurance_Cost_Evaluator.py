# Function that calculates the home insurnace price given the replacement cost of the home

def calculatePrice(houseCost): # Function calculates the home insurance coverage the user should get based on the property value
    replacement = houseCost * .80; # Coverage for 80 % of the home's value
    print("The home insurance cost for a house valued at $", houseCost,"requires a minimum insured cost of $", replacement);

def main(): # Main function is responsible for primary handling of functions and user input
    print("Home Insurance Cost Estimator");
    houseCost = int(input("Enter the replacement cost of the home: "));
    while(houseCost < 0): # Input validation
        houseCost = int(input("Enter the replacement cost of the home: "));
    calculatePrice(houseCost); # Call the calculatePrice to evaluate the dollar coverage amount need for the user's property

main();