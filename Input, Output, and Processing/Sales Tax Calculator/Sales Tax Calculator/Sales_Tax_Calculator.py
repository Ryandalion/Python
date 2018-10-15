#Function calculates the final purchase price by including state and county sales tax

price = int(input('Please enter the price for the item: '));
stateTax = .05;
countyTax = .025;

statePrice = (price + (price * stateTax));
countyPrice = (price + (price * countyTax));
totalPrice = price + (price * countyTax) + (price * stateTax);

print();
print('The price before any tax is applied: $', price, sep='');
print();
print('The price after state tax is applied: $', statePrice,sep = '');
print();
print('The price after county tax is applied: $', countyPrice, sep = '');
print();
print('The total price after all taxes are applied: $', totalPrice, sep = '');
print();
