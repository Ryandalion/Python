# Program converts user input string to pig latin

PIG = "AY"; # Create a constant PIG that helps translate the original into pig latin

def main():
    userString = input("Please enter a sentence: "); # Retrieve string from user that will be converted to pig latin
    count = 0; # Count variable initialized to zero
    tempList = []; # Create a list that will store the sentence
    tempStr = []; # Create a list that will hold the edited version of the sentence, where each word is separated into their own element
    tempList.append(userString); # Insert the string into the tempList list
    while count < len(tempList): # Loop while count is less than the number of elements in tempList
        tempList[count] = tempList[count].upper(); # Convert all elements inside tempList to upper case
        tempStr = tempList[count].split(); # Split the words inside the tempList list and assign each word to the tempStr list
        count += 1; # Increment count by one
    
    count = 0; # Count variable is set to zero.
    print("Original Sentence: ", *tempList, sep=""); # Display the original sentence. We display the list element from tempList and remove the brackets and quotations
    print("Pig Latin: ", end=" "); # Prepare user to be shown the pig latin translation
    while count < len(tempStr): # Loop while count is less than the number of elements in the tempStr list
        tempVar = tempStr[count]; # Assign tempVar the word at the index
        firstLetter = tempVar[0:1]; # Slice the string to get the first letter and assign it to firstLetter variable
        leftOver = tempVar[1:]; # Slice the string from the second letter of the sentence to the last letter of the sentence, inclusive
        print(leftOver + firstLetter + PIG, end=" "); # Now create the translated sentence -> second letter to last letter + the first letter + the constant PIG. This translates it to pig latin
        count += 1; # Increment count by one to cycle through each word

    print(); # Print newline

print("English to Pig Latin Converter\n");
main(); # Execute main

