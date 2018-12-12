# Program asks user to enter their full name (First Middle and Last name) then outputs their initials

def main():
    firstName = input("Please enter your first name: "); # Retrieve the user's first name, middle name, and last name. Store their input inside their respective variables
    middleName = input("Please enter your middle name: ");
    lastName = input("Please enter your last name: ");

    firstInitial = firstName[:1] + "."; # Slice the string of each name starting from index 0 and up to but not including index 1. Then add a period at the end of each sliced string.
    middleInitial = middleName[:1] + ".";
    lastInitial = lastName[:1] + ".";

    print();
    print("Your initials are",firstInitial.upper(), middleInitial.upper(), lastInitial.upper()); # Print the initials of the user. First name, middle name, and last name. Upper all initials.
    print();

main();