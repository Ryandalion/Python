# Program reads a text file and determines the frequency of each word. The five words are glasses(x3), difference(x4), divide(x3), wagon(x4), auction(x2)

def main():
    inputFile = open('text.txt','r'); # Program opens the text file in read only mode
    dataFile = inputFile.readlines(); # Assign the content of the text file to dataFile variable
    inputFile.close(); # Close the file object

    count = 0; # Count is used as a counter variable for the while loop
    while count < len(dataFile): # Loop while count is less than the length of the data file
        dataFile[count] = dataFile[count].rstrip('\n'); # Remove the newline characters from the data
        count += 1; # Increment by one per loop iteration

    stringConvert = ' '.join(dataFile); # Turn the list into a string by joining the list to a blank
    stringConvert = stringConvert.split(); # Split the string into separate words for analysis
    dataDict = dict(); # Initialize an empty dictionary 
    for stringConvert in stringConvert: # Loop through the whole string that contains each word
        if stringConvert in dataDict: # If the word is in the dictionary we add one to it's key
            dataDict[stringConvert] += 1;
        else: # Else the word is not in the dictionary and we just make it equal to one
            dataDict[stringConvert] = 1;

    print(dataDict); # Display the dictionary to the user

print("Number of Words Counter");
main(); # Execute main

