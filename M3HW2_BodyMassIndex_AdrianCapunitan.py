# Body Mass Index
# 6/13
# CTI-110 M3HW2 - Body Mass Index
# Adrian Capunitan
#
# Get the weight and height.
weight = int(input('Please enter the weight:'))
height = int(input('please enter the height:'))
# Calculate the BMI.
BMI = weight * 703/height**2
print ('Your BMI is',BMI)

if BMI <=18.5:
    print ('Underweight')
elif BMI >=25:
    print ('Overweight')
else: print ('Optimal')
