# Random Number File Writer
# 7/5
# CTI-110 M6HW1 - Random Number File Writer
# Adrian Capunitan
#

# Import random numbers
import random
# main function
def main():
        # open a file
        random_numbers = open('ran_numbers.txt', 'w')
        # get the number of random numbers
        qty_numbers = int(input('Input your random numbers and will be written to the file:  '))
        print('Your list of random numbers are: ')
        # create a loop to generate the random numbers in the quantity specified
        for count in range (qty_numbers):
                number = random.randint(1,500)
                # print the list of random numbers
                print(number)
        # convert the numbers to a string and write them to the file
        random_numbers.write(str(number)+ '\n')
        # close the file
        random_numbers.close()
        # tell the user the number is on file
        print('Your list of random numbers have been written to the file')
        print('ran_numbers.txt')
# close main
main()
