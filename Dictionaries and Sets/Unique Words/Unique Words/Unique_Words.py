# Program opens a text file of words and displays all unique words

def main():
    dataSet = set(open("text.txt").read().split()); # Take data from text file and put into a set
    print(dataSet); # Print the set. The set will not print duplicate words.
  
main(); # Execute main
