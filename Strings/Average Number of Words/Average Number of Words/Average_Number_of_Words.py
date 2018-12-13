# Program counts the number of words per each sentence in a text file.

def main():

    inputFile = open('text.txt','r'); # Open the text file in read only mode
    textFile = inputFile.readlines(); # Copy all the contents of the file into the textFile variable
    inputFile.close(); # Close the input file
    docLength = len(textFile); # Set docLength to the length of the textFile variable
    count = 0; # Variable responsible for counting in the loop
    numWords = 0; # Counts the number of words per sentence
    average = 0; # The average is equal to all the words in the whole document divided by the number of sentences
    totalAvg = []; # List holds the number of words per sentence
    
    while count < docLength: # Loop until count exceeds the length of the list
        textFile[count] = textFile[count].rstrip('\n'); # First remove the invisible newline characters from the textFile
       
        if "," in textFile[count]: # If there is a comma element inside the textFile list, we remove and replace it with a blank
            textFile[count] = textFile[count].replace(',','');

        if "-" in textFile[count]: # If there is a hyphen in the textFile list, we remove the hyphen and replace it with a blank
            textFile[count] = textFile[count].replace('-',' ');

        converted = textFile[count].split(); # We split the element of the list into subelements to separate all words and numbers
        index = 0; # Variable is used for indexing the subelements of the elements of the list
        numDigits = 0; # Variable is responsible for counting the number of integers that occur amongst the subelements

        # CONVERTED = LIST -> LIST ELEMENT -> LIST OF LIST ELEMENT SUB-ELEMENTS

        while index < len(converted): # Loop until index is greater than the length of the list of subelements of a list element
            if converted[index].isdigit(): # If the subelement is a digit then we increment numDigits by one and increase the index also
                numDigits += 1;
                index += 1;
            else: # The subelement is word so we increment index by one
                index += 1;
        
        numWords = len(textFile[count].split()); # Get the number of subelements within the element of the list
        numWords = numWords - numDigits; # numWords is equal to the total number of subelements minus numWords
        totalAvg.append(numWords); # Append the number of words to the totalAvg list
        count += 1; # Increment count by 1
    
    totalSum = sum(totalAvg); # Total sum is calculated using the built-in list function sum that calculates the sum of a list
    average = totalSum/docLength; # Average is equal to the sum divided by the number of elements in the textFile list (original file that derived all content from the input file)
    print("The average number of words per sentence is",average,"words"); # Print the average number of words per each sentence in the document

print("Number of Words Counter\n");
main(); # Execute main
