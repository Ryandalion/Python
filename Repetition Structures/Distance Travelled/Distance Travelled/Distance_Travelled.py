# Function that asks the user to input the number of hours they have driven and the speed at which they were driving, the program will then calculate the total distance travelled per hour

distanceTravelled = 0;

numHours = int(input("Please enter the number of hours you drove: "));
speed = int(input("Please enter the average speed of the vehicle: "));

while (numHours < 0):
    numHours = int(input("Hours cannot be negative. Please enter the number of hours you drove: "));

while(speed < 0):
    speed = int(input("Speed cannot be negative. Please enter the average speed of the vehicle: "));

print("HOUR ---------- DISTANCE TRAVELLED")
for x in range (1, numHours+1, 1):
    distanceTravelled = x * speed;
    print(x, "                   ", distanceTravelled,"miles");