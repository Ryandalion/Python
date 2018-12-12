# Program converts morse code into English characters

def main():
    # Put the morse code in a dictionary
    morseCode = {' ':' ', '--..--':',','.-.-.-':'.','..--..':'?','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H',
                 '..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N', '---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.-':'Y','--..':'Z'};

    running = 1; # Bool variable to control while loop
    execute = 1;
    message = [];

    while running != 0: # Loop while running is not equal to 0
        userCode = input("Please enter the morse code: "); # Get the morse code from the user
        englishConversion = morseCode.get(userCode,'Invalid Morse Code'); # Retrieve the value that matches the key from the morse code dictionary
        if englishConversion == 'Invalid Morse Code': # If the morse code is invalid we execute
            print("Morse code is invalid"); # Inform user that morse code is invalid
            exit(); # Exit application
        message.append(englishConversion); # Insert the value of the key into the list
        running = int(input("Would you like to enter another code? Enter 1 to continue or 0 to exit: ")); # Ask user if they wish to continue, if they enter anything other than 1 then exit program

    print();
    print("Here is the decrypted morsecode"); 
    for decrypted in message: # Print the contents of the message list
        print(str(decrypted),end="");

    print(); # Newline print

print("Morse Code Decrypter\n");
main(); # Execute main