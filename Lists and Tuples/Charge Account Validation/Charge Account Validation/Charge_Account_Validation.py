# Program loads account numbers in from a file and puts them into a list. Then the user will be asked to enter the account number and the program will sift through the list and seek the target.
# If the user specified account is found then the user will be notified that the account exists, if the account does not exist then the user will be told that the account does not exist.

def main():
    accountInfo = open('charge_accounts.txt', 'r'); # Open the charge_accounts.txt file in read only mode
    accountList = accountInfo.readlines(); # Move all data to a list titled accountList
    accountInfo.close(); # Close the file object accountInfo

    index = 0; # Create a counter variable and set it to zero

    while index < len(accountList): # Loop until index is no longer greater than length of account list
        accountList[index] = int(accountList[index].rstrip('\n')); # Remove the invisible newline character and convert the string to an integer. Then assign the integer to the index of the list
        index += 1; # Increase index by one

    print("List of account numbers");
    print(accountList); # Print the account list for testing purposes
    print();
    userNum = int(input("Please enter the account number: ")); # Retrieve the account number from user

    if userNum in accountList: # If the user's account number exists in the list then confirm to user that accounts exists
        print("Account exists");
    else: # Else inform user that the account does not exist
        print("Account does not exist");

print("Account Verification\n")
main(); # Execute main


