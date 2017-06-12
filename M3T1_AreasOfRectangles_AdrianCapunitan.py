
# Areas of Rectangle
# 6/12
# CTI-110 M3T1 - Areas of Rectangles
# Adrian Capunitan
#

# Get the dimension of rectangle1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimension of rectangle2.
length2 = int(input('Enter the length of rectagle 2:'))
width2 = int(input('Enter the width of rectangle 2:'))

# Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    print('rectangel 1 has the greatest are.')
elif area2 > area1:
    print('rectangle 2 has the greater area.')
else:
    print('both have the same area.')
