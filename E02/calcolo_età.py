import numpy as np
#import datetime
from datetime import datetime, timedelta

date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')

#mesi = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'

date = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")

datenow = datetime.now()

condizione = True
while condizione == True:
	if(date > datenow):
		condizione = False
		datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")

date = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")

datenow = datetime.now()
print(datenow.year)
print(datenow.hour)
print(datenow.second)

timediff = datenow - date

print(timediff)

#print(timediff.year)
#print(timediff.day)
#print(datenow.second)
