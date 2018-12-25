# Program simulates a retail store. It will use two different classes to allow the user to add items, edit items, remove items, get the total cost of the items, and check out

import Retail; #  Import the Retail module that will creat the item objects that will be passed to the Register objects to perform actions for buying and checking out
import Register; # Import the Register module. This module holds the functions to add, remove, calculate total, and clear cart

def main():

    userInput = 0; # Variable holds the user menu selection
    registerItem = Register.Register(); # Create a Register object via call to Register from an external module

    while userInput != 6: # Loop while user does not choose to exit
        print("1. Add new item to cart");
        print("2. View all items in cart");
        print("3. Remove item from cart");
        print("4. View total");
        print("5. Checkout and pay");
        print("6. Exit Program");
        userInput = int(input()); # Get user input and convert it to an integer to be used for the if/else statements
         
        if userInput == 1: # OPTION 1: Add new item to cart
            addCart(registerItem); # Pass the Register object as a parameter

        elif userInput == 2: # OPTION 2: View all items in cart
            print("\nItems in cart\n");
            registerItem.show_items(); # Call the Register object's show item method
            print();

        elif userInput == 3: # OPTION 3: Remove item from cart
            removeItem(registerItem); # Call the remove item method and pass the Register object as a parameter

        elif userInput == 4: # OPTION 4: View the total cost of the cart
            print("\nTotal: $", end =""); 
            registerItem.get_total(); # Call the Register object's method to calculate the total
            print();
            
        elif userInput == 5: # OPTION 5: Checkout and pay
            print("\nTransaction successful");
            print("Thank you for shopping with us\n");
            registerItem.clear(); # Clear the Register object's cart and total list

        else: # User chooses to exit
            print("\nGood-bye!\n");
            registerItem.clear(); # Clear the Register object's cart and total list



def addCart(register): # Add cart function. Get the Register object as a parameter to perform add to cart options
    userInput = 0;

    # Create the Retail objects of the items below. The intiailizer includes - Product Name, Product Description, Quantity of Product, and Price of Product
    candy = Retail.Retail("Candy", "Sugary snack", 3, 5);
    fruit = Retail.Retail("Fruit", "Vitamins", 3, 3);
    game = Retail.Retail("Game Station", "Electronic videogame machine", 2, 150);
    xPod = Retail.Retail("xPod", "Electronic tablet", 2, 100);
    book = Retail.Retail("Book", "Stack of papers", 4, 15);

    print("\nAvailable Items");
    
    while userInput != 6: # Loop while user does not choose to exit
        userInput = 0;
        print();
        print("1. Candy - $5");
        print("2. Fruits - $3");
        print("3. Game station - $150");
        print("4. xPad - $100");
        print("5. Books - $15");
        print("6. Exit");
        userInput = int(input()); # Get the user's input and convert it to an integer to be used in the if/else statements

        print();
        # IF/ELSE statements hold the items the user wishes to add to the cart
        if userInput == 1: # User chooses option 1 which is candy so we execute
            print("Candy added to cart"); # Inform user we have added item to the cart
            register.purchase_item(candy); # Use the Register object's method to purchase item which will add the Retail object's name and price to the cart and total lists found in the Register object
            
        elif userInput == 2:
            print("Fruit added to cart");
            register.purchase_item(fruit);

        elif userInput == 3:
            print("Game station added to cart");
            register.purchase_item(game);

        elif userInput == 4:
            print("xPod added to cart");
            register.purchase_item(xPod);

        elif userInput == 5:
            print("Book has been added to cart");
            register.purchase_item(book);

def removeItem(register): # Function to remove item
    print("Remove item\n");
    register.show_items(); # Call the Register object's method to show all items in the cart. This function will print the cart list found in the Register object
    userSelection = int(input("\nEnter the item number you wish to remove: ")); # Get the numeric order number associated with the user desired item they wish to delete
    register.remove_item(userSelection); # Call the Register object's method to remove the item from the cart and total list. Use the userSelection to remove the element at the index of the respected lists

print("Pytho-Mart\n");
main(); # Execute main