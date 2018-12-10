# Program will count the number of names inside the names.txt file.

def main():
    dataFile = open('names.txt','r'); # Open the names.txt file in read only mode
    firstLine = dataFile.readline(); # Retrieve the first line of the text file and assign it to the variable firstLine
    count = 0; # Set the count variable to zero. This variable will keep track of the number of names in the text file.

    while firstLine != '': # Loop while firstLine is not empty
        count += 1; # Increase count by 1
        firstLine = dataFile.readline(); # Assign first line variable to the next line in the text file
       
    dataFile.close(); # Once operation is complete, close the file object
    print("There are " + str(count) + " names in the file"); # Print the number of names in the text file

main(); # Execute main
