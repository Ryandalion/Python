# Function that measures the falling distance for an object 10 times

import math; # Import the math module to use POW function

def falling_distance(seconds): # Function calculates the falling distance using the formula d = (1/2)gt^2 and returns the distance in meters
    meters = ((1/2) * (9.8 * pow(seconds,2))); # Calculate the falling distance per second
    return meters; # Return meters

def main(): # Main function that handles output and looping
    print("SECONDS            METERS");
    for x in range(1,11): # Loop through 10 numbers starting from 1 and ending at 10
        meters = falling_distance(x); # Send x to the falling_distance fucntion
        print(x,"                 ",format(meters,'.2f')); # Print the seconds and meters

print("Falling Distance Time");
print();
main(); # Call main function to execute falling_distance program