# Program creates an email database. The user can create, lookup, and delete an email address and it's information. The program also pickles the data so the data persists even if the program is closed.

import pickle; # Import the pickle module so we can save the session data

def main():
    dictionary = initializeDictionary(); # Call the initialize dictionary function. This function will try to open an existing binary file or create a new dictionary. Regardless of the outcome, the function will return a dictionary.
    userInput = 0; # Variable that holds the user's selection from the menu
    while userInput != 5: # Loop while the user does not choose option 5 which is to exit the program
        print("1. Look up E-Mail by name");
        print("2. Add new E-Mail address");
        print("3. Delete E-Mail address");
        print("4. View all E-mail addresses");
        print("5. Exit Program");
        userInput = int(input()); # Get the user's input as an integer
        if userInput == 1: # If the user selects 1, we look up the email by name
            print("Look up E-Mail")
            userInput = input("Enter the name you are looking for: ");
            if userInput in dictionary: # If the name exists in the dictionary we print the value
                print(dictionary.get(userInput)); # Retrieve the value for the key and print
            else: # Name does not exist in the database
                print("Name does not exist in the database\n");

        elif userInput == 2: # Add a new E-Mail address
            print("Add E-Mail");
            userInput = input("Enter the name of the E-Mail owner: "); # Get the name of the E-Mail owner
            userAddress = input("Enter the E-Mail address: "); # Get the E-Mail address the owner wishes to create
            if userInput in dictionary: # If the owner's name is already in the dictionary we go to the next step
                if userAddress in dictionary: # If the email address already exists we execute next statement
                    print("E-Mail address or Name is taken\n"); # Inform user that the E-Mail address is taken
            else: # The E-Mail address is available and we append it to our dictionary
                dictionary[userInput] = userAddress; # Assign the key and value
                print("E-Mail address has been successfully added\n"); # Inform user that the E-Mail information was successfully added

        elif userInput == 3: # Delete E-Mail address
            print("Delete E-Mail");
            userInput = input("Enter the name associated with the E-Mail address: "); # Get the user's name
            if userInput in dictionary: # If the name exists in the dictionary we execute
                dictionary.pop(userInput); # Remove the key-value pair corresponding to the user's name
                print("E-Mail has been deleted\n"); # Inform user that the key-value pair has been removed
            else: # Else the name does not exist in the database and we do not remove anything
                print("Name is not associated with any E-Mail address in the database\n"); 

        elif userInput == 4: # View all E-Mail addresses
            print("View All E-Mail Addresses")
            print(list(dictionary.items())); # Print the list of dictionary items

        elif userInput >= 5: # Save all data
            saveData(dictionary); # User chooses to exit so we save data by passing dictionary to the saveData function which will pickle the data
            print("Data successfully saved");
            print("Good-Bye");   

def initializeDictionary():
    try: # Open the emailData.dat file and unpickle it and load the data into a varaible and return the variable
        inputFile = open('emailData.dat','rb');
        emailData = pickle.load(inputFile);
        inputFile.close();
        return emailData;

    except FileNotFoundError: # If there is no emailData.dat file we get an error (FileNotFoundError) and we create a new dictionary as a result and return the new dictionary to the caller
        print("No E-Mail Data");
        print("Database has been created");
        emailDict = dict(); # Create dictionary
        return emailDict;

def saveData(dictionary): # Save the dictionary data
    outputFile = open("emailData.dat","wb"); # We open the file in WB mode which is to write in binary
    pickle.dump(dictionary, outputFile); # We pickle the dictionary and store it in the outputFile
    outputFile.close(); # Close the file object

print("E-Mail Database\n");
main(); # Execute main
