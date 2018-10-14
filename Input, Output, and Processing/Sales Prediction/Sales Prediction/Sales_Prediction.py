#Function gets total projected annual sales and average sales percent, which is constant, and calculates the projected annual profit

totalSales = int(input('Please enter the projected amount of sales: '));
salesPercent = .23;
profit = (totalSales * salesPercent);

print('The projected profits for this year are $', profit, sep='');

