#Function gets as input the prices of five items and calculates the total cost w/ sales tax

sales_tax = .07;

item1 = int(input('Please enter the price for item 1: '));
item2 = int(input('Please enter the price for item 2: '));
item3 = int(input('Please enter the price for item 3: '));
item4 = int(input('Please enter the price for item 4: '));
item5 = int(input('Please enter the price for item 5: '));

subTotal = item1 + item2 + item3 + item4 + item5;
total = subTotal +  (subTotal * .07);

print();
print('The total cost for the five items before sales tax is $', subTotal, sep = '');
print('The total cost for the five items after sales tax is $', total, sep = '');


