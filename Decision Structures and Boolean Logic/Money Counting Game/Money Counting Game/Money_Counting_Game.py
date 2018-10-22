# Prorgram that asks the user to enter a certain quantity of each type of coin (penny, nickel, dime, quarter) that sums up to one dollar

print('Please enter a quantity per each coin and see if you can get exactly one dollar!');
print();
qtyPennies = int(input('Please enter the number of pennies: '));
qtyNickel = int(input('Please enter the number of nickels: '));
qtyDime = int(input('Please enter the number of dimes: '));
qtyQuarter = int(input('Please enter the number of quarters: '));

pennies = 1 * qtyPennies;
nickels = 5 * qtyNickel;
dimes = 10 * qtyDime;
quarters = 25 * qtyQuarter;

sumOfCoins = pennies + nickels + dimes + quarters;

if(sumOfCoins > 100):
    print('The amount exceeds one dollar. You lose');

elif(sumOfCoins < 100):
    print('The amount is less than one dollar. You lose');

elif(sumOfCoins == 100):
    print('The amount is equal to one dollar. Congratulations! You win!');


