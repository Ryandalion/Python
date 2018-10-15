#Function calculates conversions for ingredients based upon user's desired amount

sugar = (1.5/48);
butter = (1.0/48);
flour = (2.75/48);

userAmount = int(input("Enter the number of cookies you wish to bake: "));

sugarConvert = (sugar * userAmount);
butterConvert = (butter * userAmount);
flourConvert = (flour * userAmount);

print('Here are the measurements needed per each ingredient to make',userAmount,'cookies');
print('Sugar:', sugarConvert, 'cups');
print('Butter:', butterConvert, 'cups');
print('Flour:', flourConvert,'cups');


