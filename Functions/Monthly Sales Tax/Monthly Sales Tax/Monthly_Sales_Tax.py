# Function that calculates the county and state tax for a retail business

def stateTax(totalSales): # Function calculates the state tax. Takes totalSales as a parameter
    stateTax = (totalSales * .05); # State tax is 5%
    return stateTax;

def countyTax(totalSales): # Function calculates the county tax. Takes total sales as a parameter
    countyTax = (totalSales * .025);
    return countyTax;

def main(): # Function responsible for user input and calling the necessary functions to calculate total tax due and state and local tax
    totalSales = float(input("Enter the total sales for the month: "));
   
    while(totalSales < 0): # Input validation
        totalSales = float(input("Sales must be greater than zero. Enter the total sales for the month: "));
   
    state_tax = stateTax(totalSales); # Call function that calculates state tax and pass total sales as argument
    county_tax = countyTax(totalSales); # Call function that calculates the county tax and pass total sales as argument
    total_tax = state_tax + county_tax; # Calculate the total tax due => state tax + county tax

    print();
    print("Tax Data"); # Display tax amounts due to user
    print("County Tax Due: $", format(county_tax,'.2f'));
    print("State Tax Due: $", format(state_tax,'.2f'));
    print("Total Tax Due: $", format(total_tax,'.2f'));

print("SALES TAX CALCULATOR");
main();