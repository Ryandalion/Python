
# Program calculates a person's BMI and determines whether they are overweight, normal weight, or underweight

print('-------BMI CALCULATOR-------');
height = float(input('Please enter your height in inches: '));
weight = float(input('Please enter your weight in pounds: '));
bmi = (weight) * (703/(pow(height,2)));
print('Your BMI is', round(bmi));
if(bmi > 25):
    print('You are considered overweight according to medical standards');

elif(bmi <= 25 and bmi >= 18):
    print('You are considered normal weight according to medical standards');

elif(bmi < 18.5):
    print('You are considered under weight according to medical standards');