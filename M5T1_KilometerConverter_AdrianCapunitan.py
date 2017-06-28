# Kilometer Converter
# 6/23
# CTI-110 M5T1_KilometerConverter 
# Adrian Capunitan
#

#Write a program that ask the user to enter a distance in kilometers

conversion = 0.6214

def main():
    kilometers = float(input('Enter the distance in kilometer: '))
    show_miles(kilometers)
def show_miles(km):
    miles = km * conversion
    print (km,'kilometers is equals to', miles,'miles.')

main()
