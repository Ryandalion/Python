#Function calculates the MPG (miles per gallon) of the user's car given the miles driven and the amount of gas used

milesDriven = int(input('Please enter the number of miles you have driven: '));
gas = int(input('Please enter the number of gallons you have used: '));

mpg = (milesDriven / gas);
print('Your vehicle gets', mpg, ' miles per gallon');