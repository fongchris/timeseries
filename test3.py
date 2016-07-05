
#import matplotlib.pyplot as plt

from statistics import mean
from math import log

import csv

# set window size and number of bands
window_size = 3
number_of_bands = 200
# ten selected stocks from the US market
#stock_list = ['apple.csv','google.csv','ABBV.csv','ABT.csv','ACN.csv','MMM.csv','T.csv','NKE.csv','BAC.csv','C.csv']
stock_list = ['csv2.csv']
#stock_list = ['google.csv']
#stock_list = ['ABBV.csv']

print ("\n ")
print ("********** START OF PROGRAM ***************")
print('Input 1 - Window Size: %d' % window_size)
print('Input 2 - Number of Bands: %d' %number_of_bands)


# function 1 "extract" extracts the raw time series from the ticker
def extract(string):
	ts = []
	with open(string, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			ts.append(row[4])
	del ts[0]
	ts=list(map(float, ts))
	return ts


# function 2 "convert" converts a time serie to "tuples" of bands number
def convert(ts,window_size,number_of_bands):
	max_value = 10000
	increment = (max_value)/(number_of_bands)
	ts2 = [int ((x)//increment+1) for  x in ts]

	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
 			x = ts2[(count-window_size):count]
 			z = tuple(x)
 			ts3.append(z)
 			count = count +1
	return ts3



import collections

# function 3 "calculate_probs" calculate the probability of each alphabet
def calculate_prob (ts):
	d = dict((x,ts.count(x)/len(ts)) for x in set(ts))
	od = collections.OrderedDict(sorted(d.items()))
	return od


ts_aggregated = []
for stock in stock_list:
	ts1 = extract(stock)
	ts2 = convert(ts1,window_size,number_of_bands)
	print ('\n' )
	print ("Stock Name: %s" % stock)
	print ("Letters and Probabilities:" )
	print (calculate_prob(ts2))
	ts_aggregated = ts_aggregated + ts2


#rint ("\n ")
#print ("aggregated converted time series")
#print (ts_aggregated)



letter_prob = calculate_prob (ts_aggregated)

print ("\n ")
print ("******************* aggregated *********************")
print ("\n ")
print ("Letters and Probabilities:")
print(letter_prob)
print ("\n ")
