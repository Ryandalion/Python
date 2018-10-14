#Function converts square footage (user input) to acerage

conversion = 43560;
squareFeet = int(input('Please enter the square feet for the tract of land: '));
acreage = (squareFeet / conversion );

print(squareFeet, 'sqft converted to acres is', format(acreage, '.4f' ), 'acres');
