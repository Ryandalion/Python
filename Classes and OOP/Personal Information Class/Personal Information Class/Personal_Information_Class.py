# Program creates a personal information class that holds the user's name, address, age, and phone number for 3 people

class Person: # Create a Person class that holds 4 attributes and has 8 methods

    def __init__(self, name, address, age, number): # Class object intializer
        self.__name = name;
        self.__address = address;
        self.__age = age;
        self.__number = number;

    def set_name(self, name): # Function to set object's name
        self.__name = name;

    def set_address(self, address): # Function to set object's address
        self.__address = address;

    def set_age(self, age): # Function to set object's age
        self.__age = age;

    def set_number(self, number): # Function to set object's phone number
        self.__number = number;

    def get_name(self): # Function to retrieve object's name
        return self.__name;

    def get_address(self): # Function to retrieve object's address
        return self.__address;

    def get_age(self): # Function to retrieve object's age
        return self.__age;

    def get_number(self): # Function to retrieve object's phoe number
        return self.__number;

def main(): 
    personList = []; # Create a list to hold the Person objects
    personOne = Person("Rob", "1111 Visual Studio Ln", "22", "555-555-5555"); # Create the Person instances with initialization
    personTwo = Person("Mitch", "4444 Python Way", "19", "333-333-3333");
    personThree = Person("Marcus", "2222 OS Blvd", "33", "444-444-4444");
    
    personList.append(personOne); # Append all objects to the list
    personList.append(personTwo);
    personList.append(personThree);

    count = 0; # Counter variable for the while loop
    while count < len(personList): # Loop while count is less than the length of the list
        print(); # Print all the object's attributes
        print("Person Name:", personList[count].get_name());
        print("Age:", personList[count].get_age());
        print("Address:", personList[count].get_address());
        print("Number:", personList[count].get_number());
        count += 1;

    print();

print("Person Database");
main(); # Execute main

