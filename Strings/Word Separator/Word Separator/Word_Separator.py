# Program gets a string from the user such as "StopAndSmellTheRoses" and converts it to "Stop and smell the roses"

def main():
    userString = input("Please enter a string in this format -> StopAndSmellTheRoses: "); # Get string from user input
    convert = ''.join(' '+x if 'A' <= x <= 'Z' else x for x in userString); # Cycle through the element of each character in the string and if the element is a capital letter we add a black space after it`
    convertList = convert.split(); # Split the string and turn them into elements for a list
    count = 0;
    tempHold = convertList[0]; # Take the first word from the list and hold it in the variable
    print(tempHold,end=" "); # Print the first word then remove from the list
    converList = convertList.remove(convertList[0]); # Remove the first word from the list

    while count < len(convertList): # Loop while count is less than the length of the list
        tempString = convertList[count]; # Temp string holds the word (element) at the index of the list
        print(tempString[0].lower() + tempString[1:], end =" "); # Convert the first letter to lower case and print the remaining letters after the first letter to the end of the elements and add a space at the end
        count += 1; # Increment count by one

    print(); # Print newline

main(); # Execute main

