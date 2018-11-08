# Program calculates the future value of one's savings account

def calculateInterest(principal, interestRate, months): # Function calculates the interest accumulated for the savings account given the arguments from the user
    interestRate /= 100; # Convert the interest rate into a decimal
    futureValue = principal * pow(1 + interestRate, months); # Assign the projected balance to the future value variable
    return futureValue; # Return future value

def main(): # Function is responsible for user input and validation, calling required functions, and displaying the project account balance to the user
    principal = float(input("Enter the current savings account balance: ")); # Collect current balance of savings account
    while(principal < 0):
        principal = float(input("Account balance must be greater than zero. Enter the current savings account balance: "));

    interestRate = float(input("Enter the current interest rate: ")); # Collect the interest rate for the savings account
    while(interestRate < 0):
        interestRate = float(input("Interest rate must be greater than zero. Enter the current interest rate: "));

    months = int(input("Enter the number of months you wish to find the projection for: ")); # Collect the number of months the balance will stay in savings
    while(months < 0):
        months = int(input("Months be greater than zero. Enter the number of months you wish to find the projection for: "));

    account_value = calculateInterest(principal, interestRate, months); # Send the user's inputs as parameters to the calculate interest function and assign the return value to account_value
    print("The account will be worth $", format(account_value,'.2f'),"in",months,"months"); # Display the projected account balance to the user

print("Savings Account Future Value Calculator");
print();
main();