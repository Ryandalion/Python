# Program will generate two random numbers and create a "quiz" for the user. The two numbers will be added together and the user has to correctly answer the sum. If the user is right they will be prompted with a congraluations message

import random; # Import random module to execute random functions

def generateRandom(): # Function to generate random numbers
   num1 = random.randint(100,1000); # Generate a random number between 100 - 999
   num2 = random.randint(100,1000);
   return num1, num2; # Return num1 and num2 to main

def main():
    num1, num2 = generateRandom(); # Set num1 and num2 equal to the return values from generate random
    solution = num1 + num2; # Calculate the sum of num1 and num2
    print("Enter the correct solution"); # Display the two numbers to the user
    print();
    print(" ",num1);
    print("+",num2);
    print("------");
    print();
    userAnswer = int(input("Enter your answer: ")); # Obtain user's guess
    if(userAnswer == solution): # If the user enters the correct answer, congratulate them
        print("Congraulations, you are correct!");
    else: # Display the correct answer
        print("Sorry your answer is incorrect. The correct answer is", solution);

print("Math Quiz");
main(); # Execute main function to run program