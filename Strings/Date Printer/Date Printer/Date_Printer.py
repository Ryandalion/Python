# Program reads a date (string format: MM/DD/YYYY) and converts it to Month Day, Year

MONTHS = 12; # Constant of 12 for 12 months of the year

def main():
    userDate = input("Please enter the date that you wish to convert (MM/DD/YYYY): "); # Get the date from the user
    userDate = userDate.replace('/',""); # Replace all instances of "/" in the string with blank space (removed)
    userMonth = userDate[:2]; # Get element starting from index zero up to but not including 2. This is the month.
    userDay = userDate[2:4]; # Get element starting from index 2 up to but not including 4. This is day.
    userYear = userDate[4:9]; # Get element starting from index 4 up to but not including 9. This is year.
    dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November','December']; # Create a list of dates with each element corresponding to a month of the year.
    userMonth = dates[int(userMonth)-1]; # Assign the variable userMonth to the element found at the index specified by the userMonth variable
    print(userMonth, ",", userDay,",",userYear, sep=""); # Print out Month Day, Year and remove all spaces
    print();

print("Date Converter\n");
main(); # Execute main