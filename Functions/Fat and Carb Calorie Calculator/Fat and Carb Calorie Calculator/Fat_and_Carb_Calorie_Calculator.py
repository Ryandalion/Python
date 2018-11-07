# Function that gathers the carbohyrdates and fat the user has consumed and displays the amount of calories gained from each

def fatCalorie(fat): # Function calculates the calories gained from fat
    calFat = fat * 9; 
    print("The total calories from",fat,"grams of fat is", calFat,"calories");

def carbCalorie(carbs): # Function calculates the calories gained from carbs
    carbFat = carbs * 4;
    print("The total calories from", carbs,"grams of carbs is", carbFat, "calories");

def main(): # Function gathers user information and validates it. Then sends the arguments to their respective functions`
    fat = int(input("Enter the amount of fat in grams consumed today: ")); # Gather fat consumed from user
    while(fat < 0): # Validate user input 
        fat = int(input("Input must be greater than zero. Enter the amount of fat in grams consumed today: "));

    carbs = int(input("Enter the amount of carbs consumed today: ")); # Gather carbs consumed from user
    while(carbs < 0): # Validate user input
        carbs = int(input("Input must be greater than zero. Enter the amount of carbs consumed today: "));
    print();
    # All inputs have passed validation so we pass the variables to their respective functions
    fatCalorie(fat); # Call fatCalorie function and pass fat as argument
    print();
    carbCalorie(carbs); # Call carbCalorie function and pass carbs as argument

print("Fat and Carb to Calorie Calculator");
print();
main();