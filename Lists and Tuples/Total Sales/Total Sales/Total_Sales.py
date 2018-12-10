# Program will ask the storekeeper to enter the sales per each day for the whole week and then calculate the sum

DAYS = 7; # Days constant is set to 7 to indicate a week

def main():
    weeklySales = [0] * DAYS; # Intialize a list with 7 elements equal to zero
    item = 0; # Item variable will keep count

    while item < DAYS: # Loop while item is less than days
        sales = int(input("Enter the sales for day "+ str(item+1) + ": ")); # Get the sales for the indicated day
        weeklySales.append(sales); # Add sales to the end of the list
        item += 1; # Increment item (counter)

    totalSales = sum(weeklySales); # Use built-in sum function to calculate the sum of the list
    print("\nThe total weekly sales is $", totalSales, sep=''); # Print the total weekly sales (sum of list)

print("Weekly Sales Calculator\n")
main(); # Execute main