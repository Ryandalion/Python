# Program asks the user to enter a file name of which the first five lines will be displayed. If the file has less than five lines then all contents of the file will be displayed

def main():
    fileName = input("Enter the file name you wish to open: "); # Ask user to enter the text file name they wish to open
    fileData = open(fileName, 'r'); # Open the file name user has entered
    firstLine = fileData.readline(); # Assign the variable firstLine to the first line of the text file
    count = 0; # Initialize the variable count to zero which will be used for counting in the loop

    for count in range(1, 6): # Loop through 5 times
        print(firstLine); # Print the first line of the text file
        firstLine = fileData.readline(); # Assign firstLine to the next line

    fileData.close(); # Once loop exits we close the file pointer to ensure data has been properly saved

main(); # Call the main function
