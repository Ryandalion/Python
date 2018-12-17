# Program retrieves a user input string and calculates the number of vowels and consonants in the string

def main():
    userString = input("Please enter a string: "); # Get user input string  
    vowels = ['A','E','I','O','U']; # Create a list of vowels
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']; # Create a list of consonants
    numVowels = 0; # Holds the number of vowels
    numCon = 0; # Holds the number of consonants
    stringList = list(userString); # Converts the string into a list. We convert into a list so that each character is a single element
    count = 0; # Count is used as a counter variable
    while count < len(stringList): # Loop while count is less than the length of the list of characters
        stringList[count] = stringList[count].upper(); # Upper all characters
        count += 1; # Increment count by one

    count = 0; # Re-intialize the count variable to zero to be used in the next while loop
    while count < len(stringList): # Loop while count is less than the number of elements in the list
        if stringList[count] in vowels: # Check if the element is in the vowels list
            numVowels += 1; # If the element is a vowel we increment the number of vowels by one
        elif stringList[count] in consonants: # Check if the element is in the consonants list
            numCon +=1 ; # If the element is in the vowels list we increment by one
        count += 1;

    print("Number of vowels: ", numVowels); # Print the number of vowels
    print("Number of consonants: ", numCon); # Print the number of consonants

main(); # Execute main

