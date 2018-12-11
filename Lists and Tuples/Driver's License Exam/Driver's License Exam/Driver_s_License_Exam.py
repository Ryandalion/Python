# Program calculates the test score for a driver's license exam. The user must have a score of 75% or greater to pass the exam. 

NUM_QUESTIONS = 20; # Create a constant of 20 for 20 questions on the exam

def main():
    inputFile = open('test.txt', 'r'); # Open the test.txt file that contains all the correct answers for the exam
    testScores = inputFile.readlines(); # Copy all the contents of the file into the list - testScores
    inputFile.close(); # Close the file object
    count = 0; # Create a variable titled count and set it zero, this variable will be used for counting

    while count < NUM_QUESTIONS: # Loop until count is no longer greater than the length of list testScores
        testScores[count] = testScores[count].rstrip('\n'); # Replace the element of the list at the specified index with a revised version of the element (stripped off invisible newline character)
        count += 1; # Increment count by one per loop

    calculateScores(testScores); # Call the calculateScores function and pass the testScores list as an argument

def calculateScores(examSolutions): # Function will retrieve the student's answers and compare them to the solutions passed in as a parameter
    inputFile1 = open('user1.txt', 'r');  # Open the first student's exam
    student1 = inputFile1.readlines(); # Copy the student's exams contents to a list
    inputFile1.close(); # Close the file object
       
    inputFile2 = open('user2.txt','r'); # Open the second student's exam
    student2 = inputFile2.readlines(); # Copy the student's exams contents to a list
    inputFile2.close(); # Close the file object

    count = 0; # Set the count variable to zero
    
    while count < NUM_QUESTIONS: # Loop until count is greater than NUM_QUESTIONS (20)
        student1[count] = student1[count].rstrip('\n'); # Remove the newline character from the list that contains student one's answers
        student2[count] = student2[count].rstrip('\n'); # Remove the newline character from the list that contains student two's answers
        count += 1; # Increment count by one

    count = 0; # Re-initialize count to zero

    student_1 = 0; # Variable will hold each student's respective score
    student_2 = 0;

    while count < NUM_QUESTIONS: # Loop through the student one's exam
        if student1[count] == examSolutions[count]: # If student's answer is correct increment the student's score by one
            student_1 += 1;
            count += 1;
        else: # Else if the answer is not correct, then just increment the counter variable
            count += 1;
            
    count = 0; # Re-intialize count variable to zero and prepare it to be used for student two's check

    while count < NUM_QUESTIONS: # Conduct the same steps as above to check student two's test
        if student2[count] == examSolutions[count]: # If there is a match between the two lists, increment student two's score
            student_2 += 1;
            count += 1;
        else: # Else if there is no match increment the counter variable
            count += 1;


    if student_1 >= 15: # If student one has a score greater than or equal to 15 execute
        print("Student 1 has passed the exam with a score of", student_1,"/20");
    else:
        print("Student 1 has not passed the exam");

    if student_2 >= 15: # If student two has a score greater than or equal to 15 execute
        print("Student 2 has passed the exam with a score of", student_2,"/20");
    else:
        print("Student 2 has not passed the exam");


print("Driver's License Exam Results\n"); # Print the results
main(); # Call main
    
