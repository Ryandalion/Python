# Function that draws two different patterns of stars.. First pattern is greatest to least order.. second is least to greatest order

for y in range(7, 0, -1):
    print("*" * y);

print();
numSpaces = " ";

for x in range(0,1,1):
    for y in range(0,7,1):
        print("#" + (y * numSpaces) + "#");
