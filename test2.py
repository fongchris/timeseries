
#import matplotlib.pyplot as plt

from statistics import mean
from math import log
import csv


ts_raw = []
#0 variables and raw time serie
with open('T.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		ts_raw.append(row[4])

del ts_raw[0]

ts_raw=list(map(float, ts_raw))


#ts_raw= [21,23,22,26,29,27,27,29,30,28,28,27,29,28,31,32,33,34,35,36,37,36,35,34,35,35,36]
window_size = 3
number_of_bands = 4 
max_value = max(ts_raw)+1
min_value = min(ts_raw)
increment = (max_value+1-min_value)/(number_of_bands)

print ("\n ")
print('window size: %d' % window_size)
print('number of bands: %d' % number_of_bands)
print('maximum value: %d' % max_value)
print('increment value: %d' % increment)


print ("\n ")
print ("raw time series: ")
print (ts_raw)

ts2 = [int ((x-min_value)//increment+1) for  x in ts_raw]
print ("\n ")
print ("time series in terms of band")
print (ts2)




ts3=[]
count = 0 + window_size
while (count <= len(ts2)):
 	x = ts2[(count-window_size):count]
 	z = tuple(x)
 	ts3.append(z)
 	count = count +1
print ("\n ")
print ("time series seperated by window size")
print (ts3)




letter_prob= dict((x,ts3.count(x)/len(ts3)) for x in set(ts3))
print ("\n ")
print ("letter and probabilities ")
print(letter_prob)
print ("\n ")
