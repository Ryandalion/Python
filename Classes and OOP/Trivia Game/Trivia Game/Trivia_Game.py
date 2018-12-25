# Program is a trivia game simulator. Two players go head to head and answer 10 trivia questions.

import Question; # Import the Question module which will be used to create the questions
import Player; # Import the Player module which will be used to create the players
import random; # Import the random module which will be used to shuffle the list of questions

def main():

    userInput = 0; # User input is to control if we execute the game or exit the program

    while userInput != 2:
        print("1. Start Game");
        print("2. Exit Game");
        userInput = int(input());

        if userInput == 1:
            startGame();

def startGame(): # Function starts the game
    
    playerOne = Player.Player(0,0); # Intialize player one and player two to 0 correct answers and 0 wrong answers
    playerTwo = Player.Player(0,0);

    questionList = []; # Create a list that will hold the question objects

    # Create 10 Question objects. Each object is initialized as follows: Trivia Question, Answer 1, Answer 2, Answer 3, Answer 4, and the index of the correct answer
    Q1 = Question.Question("What is Donald Trump's middle name?", "John", "Junior", "James", "Jedd", 0);
    Q2 = Question.Question("What is the capital of Russia?", "Kiev", "St. Petersburg", "Moscow", "Leningrad", 2);
    Q3 = Question.Question("How many people died during WW II?", "30 Million", "8 Million", "63 Million", "55 Million", 3);
    Q4 = Question.Question("Which movie did Tom Hanks NOT star in?", "Cast Away", "Platoon", "The Terminal", "Catch Me If You Can", 1);
    Q5 = Question.Question("What does CPU stand for?", "Central Programming Unit", "Central Pragmatic Unit", "Central Protocol Utility", "Central Processing Unit", 3);
    Q6 = Question.Question("What year was McDonald's famous Big Mac released?", "1938", "1968", "1983", "1990", 1);
    Q7 = Question.Question("Who is the creator of Python?", "Guido Van Rossum", "Linus Torvalds", "Dennis M. Ritchie", "Bill Gates", 0);
    Q8 = Question.Question("What is the fahrenheit equivalent of 0 celsius?", "0 Fahrenheit", "32 Fahrenheit", "13 Fahrenheit", "5 Fahrenheit", 1);
    Q9 = Question.Question("Who invented the automobile?", "Henry Ford", "Ferdinand Porsche", "Karl Benz", "Thomas Edison", 2);
    Q10 = Question.Question("Which state belonged to the first colony of Jamestown?", "Pennsylvania", "Virginia", "Delaware", "Kentucky", 1);

    # Append all Question objects to the questionList list created prior to Question object initialization
    questionList.append(Q1);
    questionList.append(Q2);
    questionList.append(Q3);
    questionList.append(Q4);
    questionList.append(Q5);
    questionList.append(Q6);
    questionList.append(Q7);
    questionList.append(Q8);
    questionList.append(Q9);
    questionList.append(Q10);

    # Shuffle the list of Question objects
    random.shuffle(questionList);

    # Bool to control the switch between player one and player two per loop iteration (round)
    p1 = True;
    p2 = False;
    num = 1; # Num is the round number
    print("Game Start");
    print();
    for count in range(0,10): # Loop 10 times because there are 10 Question objects in the questionList list
        print("Player 1 Score: ", playerOne.getCorrect()); # Print player one's score (number of correct answers)
        print("Player 2 Score: ", playerTwo.getCorrect()); # Print player two's score (number of correct answers)
        print();
        if p1 == True: # If the bool for p1 is equal to True that means it is player one's turn
            print("Player 1 Turn\n");
            questionList[count].displayQuestion(num); # At the index (count) we retrieve the Question object from the list and access the retrieved Object's displayQuestion method which will print the Trivia Question associated with it
            userInput = int(input("Enter your answer: ")); # Get the user's guess
            questionList[count].userAnswer(userInput, playerOne); # Pass the user's guess to the Question object's method to check the answer and pass the Player object as well
            p1 = False; # Set player one to false so that the next loop iteration switches to player two's turn
            p2 = True; # Set player two to false so their if/else statement is executed in the next iteration
            count += 1; # Increment count by one
            print();

        elif p2 == True: # If the bool for p2 is equal to True then we execute
            print("Player 2 Turn\n");
            questionList[count].displayQuestion(num); # Retrieve the Question object at the index (count) and access the retrieved object's method to display the question. In addition, pass the num to the function to print out the question number
            userInput = int(input("Enter your answer: ")); # Retrieve the user's guess
            questionList[count].userAnswer(userInput, playerTwo);  # Call the retrieved Question object's method to check the answer. Pass the user's guess to the userAnswer method for it to be checked and pass the Player player two object as well
            p1 = True; # Set p1 bool to True so that player one's if/else statement executes for the next loop iteration
            p2 = False; # Set p2 bool to False to prevent player two's if/else statement from executing in the next loop iteration
            count += 1; # Increment count by one
            print();

        num += 1; # Increment count by one

    # After we exit the loop we determine which player won or if it is a tie
    if playerOne.getCorrect() == playerTwo.getCorrect(): # If player one's number of correct answers is equal to player two's number of correct answers then it is a tie and we inform both users
        print("It is a tie!\n");

    elif playerOne.getCorrect() > playerTwo.getCorrect(): # If player one's number of correct answers is greater than player two's number of correct answers then player one is the winner
        print("Player 1 has won!"); # Congratulate player one
        print("Player 2 got", playerTwo.getWrong(),"wrong");  # Inform player two on the number of questions they got wrong
        print();

    else: # Else player two has a higher number of correct answers than player one
        print("Player 2 has won!"); # Congratulate player two
        print("Player 1 got", playerOne.getWrong(),"wrong"); # Inform player one the number of questions they got wrong
        print();

print("Trivia Game\n");
main(); # Execute main