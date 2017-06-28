
# Feet to Inches
# 6/22
# CTI-110 M5T2_FeetToInches 
# Adrian Capunitan
#

# Convertion for inches to foot



# Function
def main():
    # Enter the feet
    feet = int(input('Enter a number of feet: '))
    # Convert to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# Convertion 
def feet_to_inches (feet):
    return feet * INCHES_PER_FOOT
INCHES_PER_FOOT = 12
main()
