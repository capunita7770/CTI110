# File Display
# 7/3
# CTI-110 M6T1 - File Display
# Adrian Capunitan
#

def main():

    # Open the file.
    myfile = open("numbers.txt", "r")

    # Read and display the file's contents.
    for line in myfile:
        number = int(line)
        print(number)

    #close the file.
    myfile.close()

main()
