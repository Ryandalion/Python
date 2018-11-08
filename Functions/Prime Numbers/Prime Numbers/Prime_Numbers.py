# Function determines whether a number is prime or not

def is_prime(number): # Function determines whether the argument is prime or not
    primeStatus = 0; # Prime status holds the result from the if-else statements. If primeStatus == 1 then the number is prime and vice versa

    if(number % 2 == 0): # Number is prime is prime if the remainder is equal to zero since it is divisible by a number other than itself or 1
        primeStatus = 1; # Set prime status to 1
    else: # Number is not prime
        primeStatus = 0; # Set prime status to 2
    return primeStatus; # Return the status

def main():
    status = 1; # Set the sentinel to 1. This variable is responsible for the while loop. If the user enters -1 they can exit the program
    print("Enter -1 to exit the loop");
    print();

    while(status != -1): # Keep looping until the user enters -1
        number = int(input("Enter the number: ")); # Get the number from the user
        if(number == -1): # User has entered -1 which means they want to exit the program
            status = -1; # Set status to -1

        elif(number == 2): # If number is equal to two we automatically determine it is prime since it complicates the external prime function
            print("The number is prime"); 
            print();
        
        else: # The user has not chosen to exit or entered 2. Proceed forward to sending the user number to the is_prime function to detrmine if it is a prime number or not
            boolStatus = is_prime(number); # Pass the number to the is_prime function and set the return value to boolStatus
            if(boolStatus == 1): # If boolStatus == 1 then the number is prime
                print("The number is prime");
                print();
            else: # Else boolStatus == 1 and the number is not prime
                print("The number is not prime");
                print();

print("Prime or Not Prime Evaluator");
print();
main();