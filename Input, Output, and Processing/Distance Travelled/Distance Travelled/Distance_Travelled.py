#Function calculates the distance a car travels at a given speed and time

speed = int(input('Please enter the speed of the vehicle: '));
time = int(input('Please enter the number of hours you wish to travel: '));
distance = (speed * time);

print('The total distance you will cover in', time,'hrs driving at', speed,'mph will be', distance, 'miles');
