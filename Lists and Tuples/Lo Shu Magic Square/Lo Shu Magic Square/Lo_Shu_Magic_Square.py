# Program simulates a Lo Shu Magic Square. A Lo Shu Magic square is a 3x3 table that results in each row having the same sum.

import random;

ROWS = 3;
COLS = 3;

def main():
    loShu = [[0,0,0],
             [0,0,0],
             [0,0,0]];
      
    for i in range(ROWS):
        for k in range(COLS):
            loShu[i][k] = int(input("Enter a number: "));

    print(loShu);

    h1 = h2 = h3 = v1 = v2 = v3 = d1 = d2 = 0; # Set the variables for the columns, rows, and diagonals

    value = loShu[0][0] + loShu[0][1] + loShu[0][2]; # Set the value to the first horizontal row. If the 2d list is a Lo Shu square then each row, column, and diagonal should share the same sum (value)

    # The if-statements below calculate and check each row, column, and diagonal of the 2d list. It checks to see if the sum of each is equal to value. If an if statement is true then we set the corresponding varaible to 1 (true). 
    if(loShu[0][0] + loShu[0][1] + loShu[0][2]) == value: # h1 = Row 0
        h1 = 1; # Set variable to true

    if(loShu[1][0] + loShu[1][1] + loShu[1][2]) == value: # h2 = Row 1
        h2 = 1;

    if(loShu[2][0] + loShu[2][1] + loShu[2][2]) == value: # h3 = Row 2
        h3 = 1;

    if(loShu[0][0] + loShu[1][0] + loShu[2][0]) == value: # v1 = Col 0
        v1 = 1;

    if(loShu[0][1] + loShu[1][1] + loShu[2][1]) == value: # v2 = Col 1
        v2 = 1;

    if(loShu[0][2] + loShu[1][2] + loShu[2][2]) == value: # v3 = Col 2
        v3 = 1;

    if(loShu[0][0] + loShu[1][1] + loShu[2][2]) == value: # d1 = Diagonal: Top Left Corner to Bottom Right Corner
        d1 = 1;

    if(loShu[2][0] + loShu[1][1] + loShu[0][2]) == value: # d2 = Diagonal: Bottom Left Corner to Top Right Corner
        d2 = 1;

    if h1 == h2 == h3 == v1 == v2 == v3 == d1 == d2 == 1: # If all varaibles are equal to 1 then it is a Lo Shu Magic Square
        print("It is a Lo Shu Square");
    else:
        print("It is not a Lo Shu Square");

print("Lo Shu Magic Square\n");
main(); # Execute main