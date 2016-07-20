#you know what final testin
#from lab
#testing 123
#import matplotlib.pyplot as plt

from statistics import mean
from math import log
import time
import csv
import timeit
import pickle
import sys



def extract(number):
	ts = []
	with open('1500comma.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			ts.append(row[number])
	del ts[0]
	ts=list(map(float, ts))
	return ts


def calculate_band (raw_value, max_value, k):
	increment = max_value/k
	if raw_value == max_value:
		band = k
	else:
		band = int(raw_value//increment+1)
	return band



def find_data_size():
	lst = []
	for i in list(range(0,1168)):
		ts = extract(i)
		lst.append(len(ts))
	print('number of stocks')
	print(lst)
	print('number of data point')
	print(len(lst))

#find_data_size()
# 1168*2517****

def find_max_min():
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = extract(stock_id)
		ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))
#find_max_min()
#1799.23  new 1469.56

def convert(ts,window_size,number_of_bands,max_value):

	#increment = (max_value)/(number_of_bands)
	#ts2 = [int ((x)//increment+1) for  x in ts]
	ts2 =[calculate_band(x,max_value,number_of_bands) for x in ts]
	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
 			x = ts2[(count-window_size):count]
 			z = tuple(x)
 			ts3.append(z)
 			count = count +1
	return ts3
'''
def calculate_prob (ts):
	ul = [(x,(ts.count(x)/len(ts))) for x in set(ts)]
	ul.sort()
	return ul
'''


def calculate_entropy (alphabet):
	prob_list=[x[1] for x in alphabet]
	#print(prob_list)
	#print(sum(prob_list))

	entropy = 0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy

def merge (ts,factor):
	merged_ts = []
	count=0
	while (count+factor-1) <= len(ts)-1:
		new_point = mean(ts[count:(count+factor)])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	return merged_ts 
#merge ([1,2,3,4,5,6],6)


def normalise(ts):
	ts_max = max(ts)
	ts_min = min(ts)
	ts_normalised = []
	for a in ts:
		if a==ts_max:
			b = 100
			ts_normalised.append(b)
		else:
			b = 100*(a-ts_min)/(ts_max-ts_min)
			ts_normalised.append(b)
	return ts_normalised





# main function 
def main(stock_list,window_size, number_of_bands, max_value):
	print ("\n ")
	
	start = timeit.default_timer()

	increment = (max_value)/(number_of_bands)
	letter_list_agg = []

	done1 = 0 
	for stock_id in stock_list:
		ts = extract(stock_id)
		ts=normalise(ts)
		ls = convert(ts,window_size,number_of_bands,max_value)
		letter_list_agg = letter_list_agg + ls
		done1 = done1+1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done1/1168))
		sys.stdout.flush()

	print ("\n ")
	print('---- done preparing data ----')
		

	data_size = len(letter_list_agg)

	unique_letter = set (letter_list_agg)

	unique_size = len(unique_letter)

	alphabet = []


	done2 =0
	for a in unique_letter:
		p=letter_list_agg.count(a)/data_size
		l = (a,p)
		alphabet.append(l)
		done2 = done2 +1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done2/unique_size))
		sys.stdout.flush()



	#ordered_letter_prob = sorted(letter_prob, key=lambda tup: tup[1], reverse=True)
	

	stop  = timeit.default_timer()
	time = (stop - start)
	
	alphabet.sort()
	
	with open('output_new.pickle', 'wb') as handle:
  		pickle.dump(alphabet, handle)

	print('\n')


	
	print(alphabet)

	
	print('-----------  n = %d, k = %d, Max = %d -------------' % (window_size, number_of_bands, max_value))

	print('\n')
	
	print('Running Time (s): %f' %time)
	print ('Sample size: %d' %data_size)


print('----  clean version ----')
stock_list = list(range(0,1168)) #1168
main(stock_list,5, 100, 100)

'''
with open('output_new.pickle', 'rb') as handle:
	a = pickle.load(handle)

non_zero = len(a)
entropy = calculate_entropy(a)
ordered_a = sorted(a, key=lambda tup: tup[1], reverse=True)

print ('Number of Non-Zero : %d' %non_zero)
print ("Entropy: %f" %entropy) 
print('Top 5:')
print(ordered_a[0:5])
'''



