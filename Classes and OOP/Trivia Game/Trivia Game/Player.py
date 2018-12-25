# Player class holds the player's score

class Player: # Class Player

    def __init__(self, correct, wrong): # Intialize correct and wrong to zero since the player has not started
        self.__correct = correct;
        self.__wrong = wrong;

    def setWrong(self): # setWrong is executed when the player gets a wrong answer and one is added to their wrong attribute per every execution
        self.__wrong = self.__wrong + 1;

    def setCorrect(self): # setCorrect is executed when the player gets an answer correct and one is added to their correct attribute per every execution
        self.__correct = self.__correct + 1;

    def getCorrect(self): # Return the number of answers the user got correct
        return self.__correct;

    def getWrong(self): # Return the number of answers the user got wrong
        return self.__wrong;

