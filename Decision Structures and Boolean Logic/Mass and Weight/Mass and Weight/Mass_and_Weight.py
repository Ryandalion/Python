# Function that mass to weight conversion

objweight = float(input('Please enter the object\'s weight in Kilograms: '));

if objweight < 0:
    print('Weight cannot be negative. Please enter a valid input: ');
else:
    calcNewton = (objweight * 9.8);
    str(calcNewton);
    if calcNewton > 500:
        print('The object is too heavy!');
    elif calcNewton < 100:
        print('The object is too light!');
    else:
        print('The weight of the object is', format(calcNewton, '.2f'),\
           'newtons');

