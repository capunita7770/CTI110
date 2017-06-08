# Tip, Tax, Total
# 6/7
# CTI-110 M2HW2 - Tip Tax Total
# Adrian Capunitan
#
Charge = float(input('Please enter the charge of food:'))

tip = Charge * 0.18

salestax = Charge * 0.07

total = Charge + tip + salestax

print ('Charge: $' + format( Charge, ',.2f'))

print ('Tip: $' + format( tip, ',.2f'))

print ('Sales Tax: $' + format( salestax, ',.2f'))

print ('Total: $' + format( total, ',.2f'))
