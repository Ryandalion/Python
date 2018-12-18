# Program creates a dictionary that contains a class name as the key and the time, room number, and instructor as the values

def main():
    courseRoom = {}; # Create an empty dictionary and assign it to course room
    courseRoom = {"CS101":"3004","CS102":"4501","CS103":"6755","NT110":"1244","CM241":"1411"}; # Insert the key-values. Course Number and Course Room 
    courseTeacher = {};
    courseTeacher = {"CS101":"Haynes","CS102":"Alvarado","CS103":"Rich","NT110":"Burke","CM241":"Lee"}; # Insert the key-values. Courese Number and Course Instructor
    courseTime = {};
    courseTime = {"CS101":"8:00 AM","CS102":"9:00 AM","CS103":"10:00 AM","NT110":"11:00 AM","CM241":"1:00 PM"}; # Insert the key-values. Course Number and Course Time

    userSelection = 0; # Variable that will hold the user's selection
    while userSelection != 5: # Loop while userSelection is not equal to 5
        print("Course Information Database"); # Print menu of choices
        print("1. Look up course room number");
        print("2. Look up course instructor");
        print("3. Look up course hours");
        print("4. Look up available courses");
        print("5. Exit Program\n");
        userSelection = int(input("Please enter your selection: ")); # Get the user selection as an integer
        print();
        if userSelection == 1: # If user selects 1, then we look up the course room number
            desc = "Room Number: ";
            executeDictionary(desc, courseRoom); # Pass the description of their option and the corresponding dictionary
        elif userSelection == 2:
            desc = "Course Instructor: "; # If user selects 2, then we look up the course instructor
            executeDictionary(desc, courseTeacher); # Pass the description and the appropriate dictionary
        elif userSelection == 3: # If user selects 3, then we look up the course hours
            desc = "Course Hours: ";
            executeDictionary(desc, courseTime); # Pass the description of their option and the appropriate dictionary
        elif userSelection == 4: # If user selects 4 then we print out the list of courses
            printCourse();
        
def printCourse(): # Print the list of courses
    print("List of courses");
    print("CS101, CS102, CS103, NT110, CM241");
    print();

def executeDictionary(desc, userDictionary): # Function takes the description and dictionary as arguments
    userInput = input("Please enter the course number: "); # Get the course number the user wishes to execute their option on
    userInput = userInput.upper(); # Uppercase the user's input
    if userInput not in userDictionary: # If the user's input does not exist in the dictionary we execute
        print("The course number does not exist");
    else: # Else the user's input exists in the dictionary and we print the description and value of the key
        print(desc, end = " "); # Print the description that was passed as an argument
        print(userDictionary.get(userInput)); # Retrieve the value of the key and print it to the user
        print();

main(); # Execute main
