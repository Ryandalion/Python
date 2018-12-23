# Program is an employee database where the user can enter the employee's ID number, name, department, and job title

import pickle; # Import pickle module to read/write binary data which allows for data persistence

class Employee: # Create a class titled Employee that holds 4 attributes and has 8 methods

    def __init__(self, name, idNumber, department, jobTitle): # Object intialization
        self.__name = name;
        self.__idNumber = idNumber;
        self.__department = department;
        self.__jobTitle = jobTitle;

    def setName(self, name): # Set the object's name
        self.__name = name;

    def setIDnum(self, idNumber): # Set the object's ID number
        self.__idNumber = idNumber;

    def setDepartment(self, department): # Set the object's department
        self.__department = department;

    def setJobTitle(self, jobTitle): # Set the object's job title
        self.__jobTitle = jobTitle;

    def getName(self): # Method to retrieve the object's name
        return self.__name;

    def getID(self): # Method to retrieve the object's ID number
        return self.__idNumber;

    def getDepartment(self): # Method to retrieve the object's department
        return self.__department;

    def getJob(self): # Method to retrieve the object's job title
        return self.__jobTitle;


def menu(): # Create the menu function

    userInput = 0; # User input responsible for user's menu choice option
    employeeDict = initializeDatabase(); # Call the intialize the database function to either retrieve existing employee data or set up and prepare the employee data structure

    while userInput != 6: # Loop while user does not choose option 6, which is to exit the program
        print("1. Enter a new employee");
        print("2. Look up employee");
        print("3. Edit employee information");
        print("4. View all employees");
        print("5. Delete Employee");
        print("6. Exit Program");
        userInput = int(input()); # Get the user's input and convert it to an integer so it can be used in the if/else statements
        
        if userInput == 1: # OPTION 1: Add new employee
            addEmployee(employeeDict); # Pass the employee database dictionary as argument

        elif userInput == 2: # OPTION 2: Look up employee
            lookupEmployee(employeeDict);

        elif userInput == 3: # OPTION 3: Edit employee information
            editEmployee(employeeDict);

        elif userInput == 4: # OPTION 4: View all employees in database
            viewEmployee(employeeDict);

        elif userInput == 5: # OPTION 5: Delete employee from the database
            deleteEmployee(employeeDict);

        elif userInput == 6: # OPTION 6: Save all data and exit program
            saveData(employeeDict); # Call function to save current data. Data can only be saved if this option is selected. If the user exits the program via other means, the data will not be saved
            print("Good-bye!");

def initializeDatabase(): # Initialize database function
    try: # Try to open .dat file
        inputFile = open("employeeData.dat","rb"); # Open the file in read binary mode
        employeeData = pickle.load(inputFile); # Unpickle the data and assign it to the employeeData variable
        inputFile.close(); # Close the file object
        return employeeData; # Return the employeeData variable to the caller

    except FileNotFoundError: # If the program tries to open the employeeData.dat file and it does not exist we will get a FileNotFoundError. If we get this error we execute this function
        print("Employee data does not exist");
        print("Initializing database now");
        employeeData = dict(); # Create a new dictionary named employeeData and return it to the caller
        return employeeData;

def addEmployee(employeeDict): # Function to add new employee
    print("Add new employee\n")
    employeeName = input("Enter the employee's name: "); # Get the new employee's name
    employeeID = int(input("Enter the employee's ID number: ")); # Get the new employee's ID number
    employeeDept = input("Enter the employee's department: "); # Get the new employee's department
    employeeTitle = input("Enter the employee's job title: "); # Get the new employee's job title
    print();
    
    newEmployee = Employee(employeeName, employeeID, employeeDept, employeeTitle); # Create a new employee object and intialize the object with the user-input variables

    employeeDict[employeeID] =  employeeName, employeeDept, employeeTitle; # Add a new key-value pair to the dicitonary. The employee ID is the key and the employee's name, department, and job title are the values

def lookupEmployee(employeeDict): # Function to look up employee
    print("Look up employee\n");
    employeeID = int(input("Enter the employee's ID number: ")); # Get the employee's ID number
    employeeHold = list(employeeDict.get(employeeID)); # Get the values associated with the employee's ID number from the dictionary and convert it to a list and assign it to employeeHold
    print("\nEmployee Information\n");
    printEmployee(employeeHold); # Pass employeeHold to the printEmployee function. We pass it as a list because the information is parsed and we can print the employee information as individual words

def editEmployee(employeeDict): # Function to edit an employee's information
    print("Edit employee information\n");
    userInput = 0; # Variable to hold the user's selection in the edit information menu
    employeeID = int(input("Enter the employee's ID number: ")); # Get the employee's ID number
    employeeHold = list(employeeDict[employeeID]); # Convert the values of the key (employee's ID number) to a list for later editing
    print("Employee Information")
    
    while userInput != 4: # Loop while the user does not choose to exit which is option 4
        print("\nPlease select an option");
        print("1. Edit name");
        print("2. Edit department");
        print("3. Edit job title");
        print("4. Exit")
        userInput = int(input()); # Get the user's input and convert it to an integer so it can be used in the if/else statements

        if userInput == 1: # OPTION 1: Edit employee's name
            newName = input("Please enter the new name: "); # Retrieve employee's new name
            employeeHold[0] = newName; # We edit the value at the 0 index of the list we converted earlier. 
            employeeDict.pop(employeeID); # We remove the key-value pair from the dictionary using the employee's ID as the key
            employeeDict[employeeID] = employeeHold; # We add a new value to the dictionary. The key is the employee's ID and the values are the 3 elements in the list
            employeeHold = list(employeeDict[employeeID]); # Update the list with the new name @ index 0

        elif userInput == 2: # OPTION 2: Edit employee's department
            newDept = input("Please enter the new department: "); # Retrieve employee's new department
            employeeHold[1] = newDept; # The employee's previous department is held in the list we created earlier at index 1. We replace the element at index 1 with the new department
            employeeDict.pop(employeeID); # Remove the key-value pair from the dictionary using the employee ID number as the key
            employeeDict[employeeID] = employeeHold; # Add a new key-value pair to the dictionary using the employee's ID as the key and the updated list as the values 
            employeeHold = list(employeeDict[employeeID]); # Update the list

        elif userInput == 3: # OPTION 3: Edit employee's job title
            newJob = input("Please enter the new job title: "); # Get the employee's new job title
            employeeHold[2] = newJob; # Replace the old job title with the new one at index 2
            employeeDict.pop(employeeID); # Remove the key-value pair in the dictionary. The key is the employee's ID number
            employeeDict[employeeID] = employeeHold; # Add new key-value pair in the dictionary. The key is the employee's ID number and the values are the updated list
            employeeHold = list(employeeDict[employeeID]); # Update the list

def viewEmployee(employeeDict): # Function to view all employees' information
    employeeHold = list(); # Create a list variable called employeeHold that will hold the employee's information in a list. The reason we put it in a list is to make it easier to present the employee's info to the user
    print("Employee Information\n");
    for i,k in employeeDict.items(): # For the key-value pairs in the dictionary (employeeDict)
        print("ID Number: ",i); # Print the key value (ID number)
        employeeHold = list(k); # Convert the value associated with key to a list assigned to employeeHold
        printEmployee(employeeHold); # Pass the list to the printEmployee function where the list is parsed and printed to the user

def deleteEmployee(employeeDict): # Function to delete an employee
    print("Delete employee\n");
    userInput = 0; # Variable used to confirm whether or not to delete the employee from the database
    employeeID = int(input("Enter the employee's ID number: ")); # Get the user's ID number that will be deleted
    print("Are you sure you want to delete the employee from the database?"); # Confirm with user that they wish to delete the employee from the database
    print("1. Confirm");
    print("2. Exit");
    userInput = int(input()); # Get user's input and convert it to an integer to be used in if/else statements

    if userInput == 1: # If user chooses 1, which is to confirm deletion, execute the removal
        employeeDict.pop(employeeID); # Remove the key-value pair from the dictionary
        print("Employee has been deleted from the database"); # Confirm to user that deletion has been successful

def printEmployee(employeeInfo): # Function to print employee's information. The parameter is a list that has been converted from dictionary values
    print("Name: ", employeeInfo[0]); # INDEX 0 => Employee's Name
    print("Department: ", employeeInfo[1]); # INDEX 1 => Employee's Department
    print("Job Title: ", employeeInfo[2]); # INDEX 2 => Employee's Job Title
    print();

def saveData(employeeDict): # Function to save the data from the current session
    outputFile = open("employeeData.dat","wb"); # Open a .dat file for writing binary
    pickle.dump(employeeDict, outputFile); # Save all the data from the current session to the file
    outputFile.close(); # Close the file object
    print("Data successfully saved"); # Confirm to user that data has been successfully saved

print("Employee Database\n");
menu(); # Print the menu to the user