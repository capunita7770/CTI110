# Sum of numbers
# 7/4
# CTI-110 M6LAB - Sum of numbers
# Adrian Capunitan
#



def main():

    total = 0

    # Open the file for reading.
    infile = open('numbers.txt', 'r')
    
    # Read three numbers from the file.
    for line in infile:
        number = int(infile.readline())
        total += number
    
    # Close the file.
    infile.close()

    print(total)

main()
