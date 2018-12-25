
class Register:

    def __init__(self): # Object initialization. Create two lists, the cart list will hold the items in the cart and the total list will hold the price of each item
        self.__cart = []; # List holds the item's names in the cart
        self.__total = []; # List holds the item's prices in the cart

    def purchase_item(self, RetailItem): # Function to purchase items. We get the RetailItem as a parameter which contains the item's information
        self.__cart.append(RetailItem.getName()); # Get the item's name and put the name inside the cart list
        self.__total.append(RetailItem.getPrice()); # Get the item's price and put the price inside the total list

    def get_total(self): # Function to calculate the total cost of all the items in the cart
        totalCost = 0; # Total cost is the sum of item's prices

        for x in self.__total: # For x in the total list we loop
            totalCost += self.__total[count]; # Total cost variable is the sum of each item's price. This line will accumulate each item's price at the index

        print(totalCost); # Print the sum of the cart's total cost to the user

    def show_items(self): # Function displays all items inside the cart
        count = 1; # Count is used for counting purposes. We will use the count variable to show the item's numeric order when we print the list to the user
        x = 0; # We initialize x to zero
        for x in self.__cart: # For x in the cart list
            print(count,". ", x, sep=""); # Print the numeric order of the index and it's respective item at the index
            count += 1; # Increment count by one

    def remove_item(self, option): # Function to remove item from the user's cart
        option = option - 1; # We subtract one from the option because of indexing
        self.__cart.pop(option); # Remove the user selected item from the cart list
        self.__total.pop(option); # Remove the user selected item from the total list
        print("Item has been removed from your cart\n"); # Inform user that item removal has been successful

    def clear(self): # Function to clear the cart. This function is called when the user exits and when the user checks out
        del self.__cart[:];
        del self.__total[:];


  
