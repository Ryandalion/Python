#Function that utilizes a while loop to calculate the calorie burn rate over a specific period of time

caloricBurn = 4.2;
caloriesBurned = 0;

for x in range(10,31,5):
    caloriesBurned += caloricBurn * x;
    print("Calories burned", caloriesBurned);

print();
print("Total calories burned over 30 minutes: ", caloriesBurned);
print();