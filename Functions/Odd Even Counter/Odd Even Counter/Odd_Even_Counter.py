# Program generates 100 random numbers and determines the number of even and odd numbers in the batch

import random; # Import random module to access randint function

def even_odd(number): # Function determines wheter the parameter is even or odd
   if(number % 2 == 0): # If the remainder of the number is zero than the number is even
       print("The random number is",number,"and it is even"); 
       print();

   else: # Number is odd
       print("The random number is",number,"and it is odd");
       print();

def main(): # Main function responsible for generating loop and sending argument to determine if even or odd
    for x in range (1, 101, 1): # Generate 100 random numbers
        number = random.randint(1,1001); # Generate a number between 1 and 1000
        even_odd(number); # Send the randomly generated number as an argument to the even_odd function where it's status will be determined

print("Even or Odd Evaluator");
print();
main();