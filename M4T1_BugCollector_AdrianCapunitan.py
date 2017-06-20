# Bug Collector
# 6/19
# CTI-110 M4T1 - Bug Collector
# Adrian Capunitan
#

# Set total = 0
# for each of 5 days:
#    Input bugs collected for a day
#    Add bugs collected to total
# Display total

total = 0

for day in range(1, 6):
    print ('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

print ('You collected a total of', total,'bugs.')
    
