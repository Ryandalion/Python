# Program capitalizes the first letter of each string input by the user.

def main():
   
    print("Please enter multiple sentences (one string per line ended with a period) and enter -1 when you are done: "); # Prompt user to enter any amount of strings under the condition that it is one per line and ended with a period.
    tempHold = []; # Create a list to hold the sentences
    running = 0; # Bool variable to control while loop
    
    while running != -1: # Keep looping until user enters -1
        userString = input(""); # Get the input from the user
        if userString == "-1": # If the user enters -1 we execute and change running to -1 and exit while loop
            running = -1; # Change the bool variable to -1
        else:
            tempHold.append(userString.capitalize()); # Input the line entered by the user into a list and capitalize the string
            
    strDisplay = " ".join(tempHold);  # Attach all the string elements together
    print(strDisplay); # Display the list as a string

main(); # Execute main
