# Program converts phone numbers that are written in characters to their number equivalent

def main():
    phoneNumber = input("Enter the phone number (XXX-XXX-XXXX): "); # Retrieve user's number
    slicedString = phoneNumber[4:12]; # Slice the string from the 4 element until the end of the number and store it in a variable
    slicedString = slicedString.upper(); # Uppercase all elements inside the variable
    number = []; # Create a list called number

    for count in range (1, len(slicedString) + 1): # Loop through the elements of slicedString which hold the last and second to last set of digits
        x = slicedString[count - 1];
        if x == 'A' or x == 'B' or  x == 'C': # If x is equal to one of the conditions append the respective value to the number list
            number.append(2);
        elif x == 'D' or x == 'E' or x == 'F':
            number.append(3);
        elif x == 'G' or x == 'H' or x == 'I':
            number.append(4);
        elif x == 'J' or x == 'K' or x == 'L':
            number.append(5);
        elif x == 'M' or x == 'N' or x == 'O':
            number.append(6);
        elif x == 'P' or x == 'Q' or x == 'R' or x == 'S':
            number.append(7);
        elif x == 'T' or x == 'U' or x == 'V':
            number.append(8);
        elif x == 'W' or x == 'X' or x == 'Y' or x == 'Z':
            number.append(9);
        elif x == '-':
            number.append("-");

    print("The converted number is ",end="");
    print(phoneNumber[:4],end=""); # Print the first 3 numbers and the hyphen
    for x in number: # Print the converted numbers from the number list
        print(str(x),end=""); # Print each number as a string and remove all spaces
    
    print(); # Newline character

print("Character to Telephone Number Converter\n");
print("Example: 555-top-GUN => 555-867-486\n");
main(); # Execute main
