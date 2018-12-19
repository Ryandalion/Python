# Program will read the contents of two text files and determine a series of results between the two, such as mutual elements, exclusive elements, etc.

def main():
    setA = set(open("file1.txt").read().split()); # Load data from file1.txt into setA
    setB = set(open("file2.txt").read().split()); # Load data from file2.txt into setB

    mutualElements = setA.intersection(setB); # Mutual Elements - Intersection between the two sets. The values found in both sets.
    unionElements = setA.union(setB); # Union Elements - The total array of elements between the two sets
    exclusiveElements = unionElements - mutualElements; # Exclusive Elements - List of elements that are exclusive to set A and exclusive to set B, combined
    setAelements = unionElements-setB; # Set A Elements - All elements exclusive to set A only
    setBelements = unionElements-setA; # Set B Elements - All elements exclusive to set B only

    print("Here is some data about the text files"); # Display the data to the user
    print("\nMutual Elements: ", mutualElements); # Mutual elements
    print();
    print("\nExclusive Elements: ", exclusiveElements); # Exclusive elements
    print();
    print("\nAll Elements: ", unionElements); # Union of set A and set B
    print();
    print("\nElements of Set A (exclusive): ", setAelements); # Exclusive elements of set A
    print();
    print("\nElements of Set B (exclusive): ", setBelements); # Exclusive elements of set B

print("Set A and Set B Analysis\n");
main(); # Execute main
