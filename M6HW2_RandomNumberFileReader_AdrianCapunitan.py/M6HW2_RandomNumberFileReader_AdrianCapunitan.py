# Random Number File Reader
# 7/6
# CTI-110 M6HW2 - Random Number File Reader
# Adrian Capunitan
#

def main():
        random_numbers = open('ran_numbers.txt', 'r')
        number = 0
        total = 0
        print("List of numbers:")
        for line in random_numbers.readlines():
              print(line)
              total = total+int(line)
              number +=1
        print("The total of the numbers = "+str(total))
        print("The number of the random numbers read from the file = "+str(number))
main()
    
