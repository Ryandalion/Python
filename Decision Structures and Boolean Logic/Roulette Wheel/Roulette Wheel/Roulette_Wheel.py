# This program simulates a roulette wheel
import random;
import time;

roll = random.randint(0,36); # Generate a random number between 0 and 36

evenOdd = roll % 2; # Check to see if roll is even or odd by evaluating the remainder. If it is zero then the number is even, odd otherwise
print('---------ROULETTE SHOWDOWN---------');
userSelection = int(input("Please enter a lucky number: "));

print('Spinning the wheel now');
time.sleep(1);
print('The ball is on number', roll);
if(userSelection == roll):
    print('It must be your lucky day! You have guessed correctly');

if (roll == 1):
    print('The ball has landed on green');

elif (roll >= 1 and roll <= 10):
    if(evenOdd == 0):
        print('The ball has landed on a even black pocket');
    else:
        print('The ball has landed on a odd red pocket');

elif (roll >= 11 and roll <= 18):
    if(evenOdd == 0):
        print('The ball has landed on a even red pocket');
    else:
        print('The ball has landed on a odd black pocket');

elif(roll >= 19 and roll <= 28):
    if(evenOdd == 0):
        print('The ball has landed on a even black pocket');
    else:
        print('The ball has landed on a odd red pocket');

elif(roll >= 29 and roll <= 36):
    if(evenOdd == 0):
        print('The ball has landed on a even red pocket');
    else:
        print('The ball has landed on a odd black pocket');

