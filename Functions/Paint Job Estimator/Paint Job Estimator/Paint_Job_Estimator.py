# Function that calculates the total cost for painting services

totalCost = 0; # Global variable to store the total costs

# Painting company can only paint 112 sqft per day and work only 8 hours per day at a rate of $35.00/hour

def calcHours(sqft): # Function that calculates the hours needed to paint the sqft
    totalHours = (sqft/112);
    print("The total hours needed to paint",sqft,"sqft is", format(totalHours,'.2f'),"hours");
    return totalHours;

def calcGals(sqft): # Function that calculates the number of gallons of paint needed to paint the sqfts
    totalGals = (sqft/112);
    print("The total gallons of paint required: ", format(totalGals,'.2f'),"gallons");
    return totalGals;

def calcLabor(sqft): # Function that calculates the labor costs based on sqft
    labor = ((35 * 8) * (sqft/112));
    print("The total labor costs are $", format(labor,'.2f'),"for",sqft,"sqft");
    global totalCost;
    totalCost += labor; # Add labor costs to total cost
    return labor;

def paintCost(sqft, galPrice): # Function that calculates the cost of paint
    paintCost = (galPrice * (sqft/112));
    global totalCost;
    totalCost += paintCost; # Add the total cost of paint to the total cost
    print("The total paint cost is $", format(paintCost,'.2f'));
    return paintCost;

def calcTotal(sqft, galPrice): # Function that calls the various other functions to execute quotes
    calcGals(sqft);
    calcHours(sqft);
    paintCost(sqft, galPrice);
    calcLabor(sqft);
    print("The total cost to paint", sqft,"sqft is $", format(totalCost,'.2f')); # Print out the total cost using the global variable
    
def main(): # Function responsible for user input validation and calling the calculate total function
    sqft = int(input("Enter the square feet of painting to be done: "));
    while(sqft < 0): # Input validation. SQFT must be greater than zero
        sqft = int(input("Number must be greater than zero. Enter the square feet of painting to be done: "));
    
    galPrice = float(input("Enter the paint's price per gallon: "));
    while(galPrice < 0): # Input validation. Price per gallon of paint must be greater than zero
        galPrice = float(input("Number must greater than zero. Enter the paint's price per gallon: "));
    print();
    calcTotal(sqft, galPrice); # Call to calculate total passing sqft and gallon of paint price as arguments

print("Paint Cost Estimator");
print();
main(); # Execute the main function
