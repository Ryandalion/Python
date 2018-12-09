# Program asks user to enter a file name to be opened. File contents will be printed on console. Each line in the file will be preceded by a number.

def main():
    fileName = input("Enter the file name you wish to open: "); # Ask user to open the text file they wish to read
    fileData = open(fileName, 'r'); # Open the requested file as read-only
    firstLine = fileData.readline(); # Assign the first line of the text file to firstLine variable
    count = 1; # Set count variable to 1. This will be used to indicate the line number that will be printed per each line

    while firstLine != '': # Loop while not empty
        firstLine = firstLine.rstrip('\n'); # Remove the "invisible" newline character from the text file
        print(firstLine + str(count)); # Print the line and append the line number, which is a int converted to a string.
        count += 1; # Increase count by one per loop iteration
        firstLine = fileData.readline(); # Assign the variable firstLine to the next line in the file
     
    fileData.close(); # Close the file after use

main(); # Execute main