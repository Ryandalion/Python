# Program determines the kinetic energy of a moving object

def kinetic_energy(mass, velocity): # Function that calculates the kinetic energy of an object given the mass and velocity
    kineticEnergy = ((1/2) * mass * (pow(velocity,2)));
    return kineticEnergy; # Return the kinetic energy of the object

def main():
    mass = float(input("Enter the object's mass: ")); # Retrieve the mass of the objecct from the user
    while(mass < 0): # Validate user input
        mass = float(input("Mass must be greater than zero. Enter the object's mass: "));

    velocity = float(input("Enter the object's velocity: ")); # Retrieve the velocity of the object from the user
    while(velocity < 0): # Validate user input
        velocity = float(input("Velocity must be greater than zero. Enter the object's velocity: "));

    kineticEnergy = kinetic_energy(mass, velocity); # Call the kinetic_energy function and pass the mass and velocity as arguments and assign the return value from kinetic_energy to kineticEnergy

    print();
    print("The kinetic energy of the object is ", format(kineticEnergy,'.2f'), "J", sep = ""); # Display the kinetic energy of the object to the user

print("Kinetic Energy of an Object");
print();
main();

