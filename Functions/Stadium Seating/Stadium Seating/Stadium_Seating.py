# Program gathers sales data for 3 different sections in a stadium and calculates the total revenue

def calcTotal(sectionA, sectionB, sectionC): # Function that calculates the total sales from all sections
    totalSales =(sectionA * 20) + (sectionB * 15) + (sectionC * 10); # Multiply the number of seats sold per section by their respective seat price
    print();
    print("The total sales from all sections is $", totalSales); # Print the total sales numbers to the user

def main():
    sectionA = int(input("Enter the number of seats sold in Section A: ")); # Gather sales data for section A
    while(sectionA < 0): # Validate user input
         sectionA = int(input("Number sold must be greater than zero. Enter the number of seats sold in Section A: "));

    sectionB = int(input("Enter the number of seats sold in Section B: ")); # Gather sales data for section B
    while(sectionB < 0): # Validate user input
        sectionB = int(input("Number sold must be greater than zero. Enter the number of seats sold in Section B: "));

    sectionC = int(input("Enter the number of seats sold in Section C: ")); # Gather sales data for section C
    while(sectionC < 0): # Validate user input
        sectionC = int(input("Number sold must be greater than zero. Enter the number of seats sold in Section C: "));

    calcTotal(sectionA, sectionB, sectionC); # Send all section quantity sold values to the calculate total sales function
   
print("Total Sales Calculator");
print();
main(); # Execute main to execute main program function