# Question class contains a question, 4 possible answers, and the number of correct answers

class Question: # Question Class attributes and methods

    def __init__(self, trivia, a1, a2, a3, a4, answerNum): # Intialize the object with the trivia question, the 4 possible answers, and the index of the correct answer
        self.__trivia = trivia;
        self.__a1 = a1;
        self.__a2 = a2;
        self.__a3 = a3;
        self.__a4 = a4;
        self.__answerNum = answerNum;

    def displayQuestion(self, num): # Object method to display the question
        print("Question",num,": ",self.__trivia);
        print("Select the correct answer");
        print("1.", self.__a1);
        print("2.", self.__a2);
        print("3.", self.__a3);
        print("4.", self.__a4);

    def userAnswer(self, option, Player): # Object method to retrieve the user's answer and determine if it is wrong or correct. The parameters are option (player's selection) and the Player object
        option -= 1; # Deduct the player's option by one due to indexing
        if option == self.__answerNum: # If the user's answer is equal the object's indexed answer then execute
            print("\nYou are correct!"); # Congratulate user that they are correct
            Player.setCorrect(); # Call the Player object parameter that was passed and execute the setCorrect method which will increment the Player object's correct variable by one
        else: # Else the answer is wrong and we inform the user and provide them with the correct answer's index
            print("\nThat is incorrect. The correct answer is", self.__answerNum + 1);
            Player.setWrong(); # Call the Player object's method and increment the object's wrong variable by one



