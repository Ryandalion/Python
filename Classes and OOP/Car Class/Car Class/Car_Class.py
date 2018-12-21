# Program consists of a car class that has various attributes and methods

class Car: # Class Car contains 3 attributes - Year, Maker, and Speed. Class also contains three methods - Accelerate (+5), Brake (-5), and Get Speed

    def __init__(self, year, make, speed): # Initialize with car year, car maker, car speed
        self.__year = year;
        self.__make = make;
        self.__speed = speed;

    def accelerate(self): # Accelerate method
        self.__speed += 5; # Add five to object's speed

    def brake(self): # Brake method
        self.__speed -= 5; # Subtract five from the object's speed
  
    def getSpeed(self): # Display the speed to the user
        return self.__speed; # Return the speed of the objecct to the user

def main():
    vehicle1 = Car(2020, "HoverCar", 50); # Initialize one Car object with the following parameters
    for x in range (0,5): # Loop five times and accelerate the vehicle per loop iteration
        vehicle1.accelerate(); # Call the object's accelerate method which increases the vehicle's speed by 5mph per iteration

    print("Speed of vehicle one after accelerating five times",vehicle1.getSpeed(),"mph"); # Display the speed of the vehicle after accelerating five times

    for x in range(0,5): # Loop five times and call the brake method per loop iteration
        vehicle1.brake(); # Call the object's method which decreases the vehicle's speed per loop iteration

    print("Speed of vehicle one after braking five times", vehicle1.getSpeed(),"mph"); # Display the vehicle's new speed after braking five times


print("Vehicle Speed - Accelerate and Brake")
main(); # Execute main