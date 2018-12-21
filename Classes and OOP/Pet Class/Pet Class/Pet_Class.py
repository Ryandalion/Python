# Program creates a pet class that has multiple methods and variaables

class Pets: # Create a class named Pets. This class has 3 attributes: name, animal type (species), and age. It also has six methods which are set name, set age, set species, get name, get age, get species/

    def __init__(self, name, animalType, age): # Class object intializer
        self.__name = name; # Name
        self.__animal_type = animalType; # Animal type
        self.__age = age; # Animal age

    def set_name(self, name): # Function to set the name of the object
        self.__name = name;

    def set_animal_type(self, animalType): # Function to set the animal type of the object
        self.__animal_type = animalType;
      
    def set_age(self, age): # Function to set the age of the object
        self.__age = age;

    def get_name(self): # Function to retrieve the object's name
        return self.__name;

    def get_animal_type(self): # Function to retrieve the object's animal type
        return self.__animal_type;

    def get_age(self): # Function to retrieve the animal's age
        return self.__age;

def menu(): # Print the menu to the user
   
    userInput = 0; # Variable holds user selection
    animalList = []; # Create a list to hold the animal information

    while userInput != 5: # Loop while user does not choose to exit (5)
        print("1. Add new animal");
        print("2. Edit animal information");
        print("3. View animal information");
        print("4. View all animals");
        print("5. Exit Program");
        userInput = int(input()); # Get user input and convert it to an integer

        if userInput == 1: # Option 1: Add new animal
            print();
            animalList = addAnimal(animalList);
        elif userInput == 2: # Option 2: Edit an existing animal
            print();
            animalList = editAnimal(animalList);
        elif userInput == 3: # Option 3: View a specific animal's details
            print();
            viewAnimal(animalList);
        elif userInput == 4: # Option 4: View all animals in the list
            print();
            viewAll(animalList);
        print(); # Print a newline

def addAnimal(animalDirectory): # Function to add a new animal
    newAnimal = Pets("","",0); # Create a new object instance of the class Pets
    animalName = input("Enter the animal's name: "); # Get the name of the animal
    animalAge = int(input("Enter the animal's age: ")); # Get the age of the animal
    animalSpecies = input("Enter the animal's species: "); # Get the species of the animal

    newAnimal.set_name(animalName); # Set the object's name
    newAnimal.set_age(animalAge); # Set the object's age
    newAnimal.set_animal_type(animalSpecies); # Set the object's species

    animalDirectory.append(newAnimal); # Append the object to the list
    return animalDirectory; # Return the list to the caller

def editAnimal(animalDirectory): # Function to edit an animal's information - Name and Age
    animalName = input("Enter animal's name you wish to edit: "); # Get the animal's name
    x = 0; # Variable used for counting in the while loop
    found = False; # Found determines if the animal's name was found in the list
    while x < len(animalDirectory): # Loop while x is less than the length of the list
        if animalName == animalDirectory[x].get_name(): # If the user input name is equal to a name in the list then we execute
            print("Please select what you would like to edit"); # Ask user what they would like to edit - Name or Age
            print("1. Name");
            print("2. Age");
            userInput = int(input());  # Get user's option

            if userInput == 1: # Option 1: User chooses to edit an existing animal's name
                newName = input("Enter the animal's new name: "); # Get the new name from the user
                animalDirectory[x].set_name(newName); # Set the new name of the object
                print("Name successfully updated"); # Inform user that the name has been successfully updated
                x += 1; # Increment x by one
                found = True; # Set the bool flag to true. The name has been found
                return animalDirectory; # Return the directory to the caller

            elif userInput == 2: # Option 2: User chooses to change an existing animal's age
                newAge = input("Enter the animal's new age: "); # Get the new age from the user
                animalDirectory[x].set_age(newAge); # Set the object's new age
                print("Age successfully updated"); # Inform user that update was successful
                x += 1; # Increment x
                found = True; # set bool to true since we have found target
                return animalDirectory; # Return the list
        else: # No match at index so we increment x to go to next object in list
            x+=1;

    if found == False: # If the found flag is still false after looping through all elements we inform user that the name was not found in the list
        print("Animal is not in database");

def viewAnimal(animalDirectory): # Function to print a user-specified animal's information
    seekAnimal = input("Enter the animal's name: "); # Get the animal's name
    count = 0; # Count is a counter variable for the while loop
    while count < len(animalDirectory): # Loop while count is less than the length of the list
        if seekAnimal == animalDirectory[count].get_name(): # If the user specified name is found in the list we execute
            print("Animal Name:", animalDirectory[count].get_name()); # Print the name of the object at the index
            print("Animal Age:", animalDirectory[count].get_age()); # Print the age of the object at the index
            print("Animal Species:", animalDirectory[count].get_animal_type()); # Print the animal type of the object at the index 
            count += 1; # Increment count
        else:
            count += 1; # Increment count

def viewAll(animalDirectory): # Function prints all animal's information
    print("Animals in database\n");
    count = 0; # Counter variable for while loop
    while count < len(animalDirectory): # Loop while count is less than the length of the list
        print("Animal Name:", animalDirectory[count].get_name()); # Print the object's name
        print("Animal Age:", animalDirectory[count].get_age()); # Print the object's age
        print("Animal Species:", animalDirectory[count].get_animal_type(),"\n"); # Print the object's animal type
        count += 1; # Increment count by one


print("Veterinary Database");
menu(); # Execute the menu