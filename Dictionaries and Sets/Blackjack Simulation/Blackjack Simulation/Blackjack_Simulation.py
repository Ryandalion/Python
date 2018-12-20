# Program is a blackjack simulator

import random; # Random module is needed to perform random choice operation on deck of cards

def main():
    deck = create_deck(); # Call the create deck function to create a dictionary of cards
    userInput = 0; # User menu selection

    while userInput != 2: # Loop while the user has not chosen option 2, which is to exit the program
        print("1. Start Game");
        print("2. Exit Game");
        userInput = int(input()); # Convert the user's option to an integer
        if userInput == 1: # If the user has chosen option 1, we execute the dealing of cards
            deal_cards(deck);

def create_deck(): # Function creates a dictionary that mimics a card deck and returns the dictionary to the caller

    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck;


def deal_cards(deck): # Function to deal the cards
    playerOne = 0; # Player one score
    playerTwo = 0; # Player two score
    oneHand = ""; # Player one hand. Holds the card type
    twoHand = "", # Player two hand. Holds the card type
    oneTotal = 0; # Player one's total score
    twoTotal = 0; # Player two's total score
    round = 1; # Round variable is used to display the round number to the user
    count = 0; # Start at three since we always have to deal two cards to each player
    running = True; # Bool variable to control the while loop
    deckLength = len(deck); # Length of the deck
    usedCards = [];

    while running != False:        
        
        oneHand, playerOne = random.choice(list(deck.items())); # Deal the cards to each player
        twoHand, playerTwo = random.choice(list(deck.items())); 

        deck.pop(oneHand); # Remove player one's card from the deck
        deck.pop(twoHand); # Remove player two's card from the deck

        if playerOne == 1: # If player one has pulled an Ace whose value is initialized to 1 we execute
            if oneTotal < 21: # If player one's total score is less than 21, we execute
                playerOne = 11; # Assign the value of 11 to the Ace

        if playerTwo == 1: # If player two has pulled an Ace whose value is initially one we execute
            if twoTotal < 21: # If player two's total score is less than 21 we execute
                playerTwo = 11; # We assign the value of 11 to the Ace

        oneTotal += playerOne; # Update player one's total score
        twoTotal += playerTwo; # Update player two's total score

        print("\nRound",round); # Print the round number
        print("Player One's Hand:",oneHand); # Print player one's card that was dealt for the round
        print("Player One's Score:", oneTotal); # Print player one's total score
        print("Player Two's Hand:",twoHand);  # Print player two's card that was dealt for the round
        print("Player Two's Score:", twoTotal); # Print player two's total score

        if oneTotal == 21: # If player one's total score is equal to 21, they have hit blackjack and we inform both parties
            print("\nPlayer One hit blackjack. Player one wins");
            running = False; # Set bool to false to exit while loop

        elif twoTotal == 21: # If player two's total score is 21 they have hit blackjack and we inform both parties
            print("\nPlayer Two hit blackjack. Player two wins");
            running = False; # Set bool to false to exit while loop

        elif count == deckLength: # If the count variable is equal to the length of the deck, that means we have used all the cards 
            running = False; # Set bool to false to exit while loop
            print("\nNo more cards in the deck. It is a tie");
            printFinal(oneTotal, twoTotal); # Print the final score by passing the total scores of both parties to the print final function

        elif oneTotal > 21 and twoTotal > 21: # If player one and player two's total scores exceed 21, that means they have both lost and it's a tie
            print("\nIt is a tie");
            printFinal(oneTotal, twoTotal); # Print the final score for each player
            running = False; # Set bool to false to exit while loop

        elif oneTotal > 21: # If player one's total score has exceeded 21, that means player two has won and we inform both parties
            print("\nPlayer 2 has won");
            printFinal(oneTotal, twoTotal); # Print the final score of both parties
            running = False; # Set bool to false to exit while loop

        elif twoTotal > 21: # If player two's total score exceeds 21, that means player one has won and we inform both parties
            print("\nPlayer 1 has won");
            printFinal(oneTotal, twoTotal); # Print the final score of both players
            running = False; # Set bool to false to exit while loop

        count += 2; # Increment count by 2 per each loop iteration because we deal two cards per round. One card for player one and one card for player two.
        round += 1; # Increment the round number by one per loop iteration
       
def printFinal(playerOne, playerTwo): # Function prints the final score of both players after an event is triggered
    print("\nFinal Score");
    print("Player One:", playerOne); # playerOne = oneTotal
    print("Player Two:", playerTwo); # playerTwo = twoTotal
    print();

print("Blackjack Simulator\n");
main() # Execute main

