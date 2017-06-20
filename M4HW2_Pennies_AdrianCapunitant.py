# Pennies
# 6/19
# CTI-110 M4HW2 - Pennies for Pay 
# Adrian Capunitan
#


NoofDays = int(input('How many days you worked? '))
totalEarn = 0
    
for days in range ( NoofDays ):
    penniesForTheDay = (2 ** days)/100
    totalEarn += penniesForTheDay
    print (penniesForTheDay)

print ('Total Earn:',totalEarn)
    
