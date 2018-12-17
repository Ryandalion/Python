# Program gets a string as input from the user and determines the most frequent character in the string.

def main():
    charList = {}; # Create a dictionary
    charList = {'A':0, 'B':0, 'C':0, 'D':0,'E':0, 'F':0, 'G':0,'H':0, 'I':0,'K':0, 'L':0, 'M':0, 'N':0, 'O':0 ,'P':0, 'Q':0, 'R':0, 'S':0,'T':0, 'V':0, 'X':0,'Y':0, 'Z':0}; # Intialize the dictionary with the keys being the letters of the alphabet and the values being zero.
    userString = input("Please enter a string: "); # Get the string from the user
    userList = list(userString); # Seperate the charcters of the string into individual elements
    count = 0; # Create a count variable to be used for counting
    while count < len(userList): # Loop while count is less than the number of elements in the userList
        letter = userList[count].upper(); # Intialize letter to the element at the index
        if letter in charList: # If the letter is in the charList dictionary we execute
           tempValue = charList.get(letter); # Get the value at the current key (letter)
           tempValue += 1; # Increment the value by one 
           charList[letter] = tempValue; # Assign the new value of the key
           count += 1; # Increment count by one
        else: # If the character is not a letter we execute
            count += 1; # Increment count by one

    print("The most frequent character is ", max(charList, key=charList.get),". It appears ",max(charList.values())," times",sep=""); # Display the most common character and the number of times it occurs

main(); # Execute main