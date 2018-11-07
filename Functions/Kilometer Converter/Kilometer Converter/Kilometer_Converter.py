# Program uses a function to convert kph to mph

def convertKPH(kph): # Function that converts KPH to MPH. It takes kph as a parameter and converts it to mph
    mph = kph * .6214;
    print("The conversion of",kph,"kph to mph is", format(mph, '.2f'), "mph");

def main(): # Main is responsible for getting user input and calling the conversion function
    kph = int(input("Enter the kph speed you wish to convert to mph: "));
    while(kph < 0): # Validate user input to make sure they do not enter a negative speed
        int(input("Speed cannot be negative. Enter the kph you wish to convert to mph: "));
    convertKPH(kph); # If user input is validated we call the conversion and pass kph as an argument

main(); # Call main to begin execution of all functions