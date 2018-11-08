# Program asks the user for five test scores and determines the letter grade for the test score and the average of all the test scores

def calc_average(averageScore, score): # Function that accumulates all the scores to be average later
    averageScore += score;
    return averageScore; 

def determine_grade(score): # Function that determines the student's letter grade based on their numeric grade
    if(score < 60):
        print("Student got a F");
    elif(score >= 60 and score <= 69):
        print("Student got a D");
    elif(score >= 70 and score <= 79):
        print("Student got a C");
    elif(score >= 80 and score <= 89):
        print("Student got a B");
    elif(score >= 90 and score <= 100):
        print("Student got a A");

def main(): # Main function that validates uesr input and loops through the functions 5 times.
    totalScore = 0; # Variable will hold the total score. This store grows per each iteration of calc_average call
    averageScore = 0; # Variable is the average score it will accumulate per each call to calc_average

    for x in range(1,6): # Loop through the function calls 5 times because there are five students
        print("Enter student",x,"'s score: ");
        userScore = float(input());
        
        while(userScore < 0): # Input validation
            userScore = float(input("Score must be greater than zero. Enter student",x,"'s score: "));

        totalScore += calc_average(averageScore, userScore); # Send the student's score and the average score as arguments to the calc_average function
        determine_grade(userScore); # Determine the letter grade of the student based on the user's numeric grade
        print();

    totalScore /= 5; # Divide the total score by five to get the average score
    print("The average score is", totalScore); # Display the average score to the user

print("Test Grade Analyzer");
print();
main();