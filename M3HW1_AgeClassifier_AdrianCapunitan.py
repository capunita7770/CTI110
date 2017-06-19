# A brief description of the project
# 6/12
# CTI-110 M3HW1 - Age Classifier
# Adrian Capunitan
#

age = int(input('Enter the persons age:'))

if age<= 1:
    print('The person is an infant')
elif age<13:
    print('The person is a child')
elif age<20:
    print('The person is a teenager')
elif age>=20:
    print('The person is an adult')
