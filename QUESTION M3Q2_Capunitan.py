# Question M3Q2A-M 
# (Adrian Capunitan)
# (6/13/2017)

temp = float(input ("What is the temperature sample in Fahrenheit Degree?"))

if temp <=32:
    print ('Solid state')
elif temp <212:
    print ('Liquid state')
else:
#Temp is too hot
    print ('gas')
