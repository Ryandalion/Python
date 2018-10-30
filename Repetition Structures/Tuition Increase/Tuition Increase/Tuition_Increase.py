# Function that calculates the projected semester tuition amount for next 5 years conditional to a 3 percent increase in tuition each year

tuition = 8000;
increase = 0;
rate = .08;
totalCost = 0;

for x in range (0, 5, 1):
    for y in range(0,4,1):
        totalCost += tuition;
    print("Tuition for year " + str(x + 1) + " is: $", format(totalCost,'.2f'));
    tuition += (tuition * rate);
    totalCost = 0;
