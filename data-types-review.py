#EXERCISE 2

#Question 1

import math

Vsphere = 4/3 * math.pi * 5**3
print (Vsphere)

#Question 2

bookCost = 24.95*60 / 1.4 + 3 + 0.75*60
print (bookCost)

#Question 3

leftAt = 60*(6*60) + 52*60
easyPace = 2*(8*60 + 15)
tempoPace = 3*(7*60 + 12)
totSeconds = leftAt + easyPace + tempoPace
print (totSeconds)

totMins = totSeconds/60
print (totMins)

totHrs = totMins//60
totMins = totMins%60

print (f'{totHrs:.0f}:{totMins:.0f}')

#Question 3 using datetime library

from datetime import timedelta

leftAt = timedelta(hours = 6, minutes = 52)
easyPace = timedelta(minutes = 8, seconds = 15)
tempoPace = timedelta(minutes = 7, seconds = 12)

breakfast = leftAt + 2*easyPace + 3*tempoPace
print (breakfast)

#EXERCISE 3

p = 110000
r = 0.725/12
n = 12*30

m = p*(r/(1-(1+r)**(-n)))
print (f'${m:.2f}')