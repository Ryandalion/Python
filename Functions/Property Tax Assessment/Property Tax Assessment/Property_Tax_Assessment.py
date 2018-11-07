# Function calculates the property tax for a given piece of property

def calculateTax(propertyValue): # Function calculates the property's assessment value and the tax rate for the property
    propertyValue *= .60; # Assessment value is 60% of the property value
    print("The assessment value of the property is $", format(propertyValue,'.2f')); # Print the assessment value to the user
    propertyValue /= 100; # Divide assessed value by 100 because the property tax rate is calculated per $100
    taxAmount = (propertyValue * .72); # Multiply the assessed rate by .72 because there is a 72 cent tax per $100 property value
    print("The total tax amount for the property is $", format(taxAmount,'.2f')); # Print the total tax amount to the user
    
def main():
    propertyValue = int(input("Please enter the property's value: ")); # Ask user to enter the property's dollar value
    while(propertyValue < 0): # User input validation
        propertyValue = int(input("Please enter the property's value: "));
    calculateTax(propertyValue); # Pass the property value as an argument to the tax calculator

print("Property Tax Calculator");
print();
main(); # Call main function to execute all 