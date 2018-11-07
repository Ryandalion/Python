# Function calculates the monthly and annual costs for automobile maintenace

def calculateMonthly(): # Function gathers user expenses and sums all payments. Function then prints monthly cost and sends the total cost as an argument to the annual calculator function
    loanPayment = int(input("Enter the monthly loan payment: "));
    insuranceCost = int(input("Enter the monthly insurance cost: "));
    gasCost = int(input("Enter the monthly gas cost: "));
    oilCost = int(input("Enter the monthly oil cost: "));
    tireCost = int(input("Enter the monthly tire cost: "));
    maintenanceCost  = int(input("Enter the monthly maintenance cost: "));
    print();
    totalCost = loanPayment + insuranceCost + gasCost + oilCost + tireCost + maintenanceCost; # Calculate total cost
    print("Monthly Car Expenses");
    print("The monthly cost for all expenses is $", totalCost); # Print monthly total cost
    print();
    calculateAnnual(totalCost); # Pass total monthly cost to calculateAnnual
    
def calculateAnnual(totalCost): # Function gets monthly cost as parameter
    annualCost = totalCost * 12; # Calculate annual cost by multiplying the total cost by 12
    print("Annual Car Expenses");
    print("The annual cost for all expenses is $", annualCost); # Print the annual cost of automobile expenses

print("Car Expense Calculator");
calculateMonthly(); # Call calculate monthly function to begin execution