# Function that calculates the number of hot dog packages needed
import math

numPeople = int(input("Enter the number of people coming to your hotdog party: "));
numHotDogs = int(input("Enter the number of hotdogs each person will receive: "));

totalDogs = numPeople * numHotDogs; #Calculate the total number of hotdogs. This is derived from number of guests multiplied by the number of hotdogs distributed to each guest

qtyDogs = math.floor(totalDogs / 10); # Get the number of hotdog packages needed. Each hotdog pack contains 10 weiners.
qtyBuns = math.floor(totalDogs / 8); # Get the number of buns needed. Each bun pack contains 8 buns.

dogsLeftover = totalDogs % 10; # Get the leftover amount of hotdogs by executing modulo 
bunsLeftover = totalDogs % 8; # Get the number of buns leftover by using modulo

print("\nThe minimum number of hotdog packages needed is:", qtyDogs);
print("The minimum number of hotdog bun packages needed is:", qtyBuns);
print("The number of hotdog sausages that will be leftover is:", dogsLeftover);
print("The number of hotdog buns that will be leftover is:", bunsLeftover)
