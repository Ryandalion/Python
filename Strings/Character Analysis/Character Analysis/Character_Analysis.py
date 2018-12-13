# Program reads a text file and determines the number of lowercase, uppercase, digits, and whitespace characters in the file.

def main():
    inputFile = open('text.txt','r'); # Open the text file in read only mode
    textFile = inputFile.readlines(); # Copy all of the text file contents into the textFile list variable
    inputFile.close(); # Close the file object

    count = 0; # Variable responsible for counting in the while loop
    upperCase = 0; # Holds the number of uppercase letter occurences in text
    lowerCase = 0; # Holds the number of lowercase letter occurences in the text
    numDigit = 0; # Holds the number of digits that occur in the text
    whiteSpace = 0; # Holds the number of white spaces that occur in the text

    textLength = len(textFile); # Get the length of the textLength variable

    while count < textLength: # Loop until count is greater than textLength
        textFile[count] = textFile[count].rstrip('\n'); # Remove all the invisible newline characters
        copyString = textFile[count]; # Copy the list element to the variable copy string
        print(copyString); # Print the copyString variable to show the line that is selected`
        copyLength = len(copyString); # Get the length of the string
        innerIndex = 0; # Initialize a innerIndex for counting inside the string
        while innerIndex < copyLength: # Loop until the inner index is greater than the length of the string
            if copyString[innerIndex].isdigit() == True: # If the element at the index is a number we execute
                    numDigit += 1; # Increase numDigit variable by one
                    innerIndex += 1; # Increase the inner index
            elif copyString[innerIndex].isalpha() == True: # If the element at the index is a alphabetic character we execute
                if copyString[innerIndex].islower() == True: # If the element is lowercase we execute
                    lowerCase += 1; # Increment lowerCase variable by one
                    innerIndex += 1;
                else: # Else the character is upperCase and we execute
                    upperCase += 1; # Increment upperCase variable by one
                    innerIndex += 1;
            elif copyString[innerIndex].isspace() == True: # If the element at the index is a white space we execute
                    whiteSpace += 1; # Increment white space variable by one
                    innerIndex += 1;
            else: # If the element at the index is none then we just increment the counter variable innerIndex
                innerIndex += 1;
        
        count += 1; # Increment count variable which controls main while loop

    print();
    print("Analysis Results\n"); # Print results to the user
    print("Number of uppercase characters: ", upperCase);
    print("Number of lowercase characters: ", lowerCase);
    print("Number of whitespaces: ", whiteSpace);
    print("Number of digits: ", numDigit);
    print();
   

print("Text Analayzer\n");
main(); # Execute main
