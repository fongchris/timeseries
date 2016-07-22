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



def convert_s(ts,window_size,number_of_bands,max_value):

	ts2 =[calculate_band(x,max_value,number_of_bands) for x in ts]
	ts3=[]
	count = 0 + window_size
	while (count <= len(ts2)):
				x = ts2[(count-window_size):count]
				z =''
				for i in x:
					z=z+str(i)+','
				ts3.append(z)
				count = count +1
	return ts3





def calculate_entropy (alphabet):
	prob_list=[x[1] for x in alphabet]
	#print(prob_list)
	#print(sum(prob_list))

	entropy = 0.0
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




# ============= conversion ===============
def spliting(a_string):
	a = a_string[:-1] 
	b = a.split(',')
	c = tuple([int(x) for x in b])
	return c


def conversion (alphabet_s):
	new_alphabet = [] 
	for item in alphabet_s:
		x = (spliting(item[0]),item[1])
		new_alphabet.append(x)
	return new_alphabet


# main function 

def main(stock_list,window_size, number_of_bands, max_value):
	print ("\n ")
	
	start = timeit.default_timer()

	increment = (max_value)/(number_of_bands)
	letter_list_agg = []

	done1 = 0 
	for stock_id in stock_list:
		
		#============ Changes ===============************
		ts = extract(stock_id)

		master_list = []

		master_list.append(ts[0:500]) # 0-499
		master_list.append(ts[500:1000]) #500-999
		master_list.append(ts[1000:1500])#1000-1499
		master_list.append(ts[1500:2000])#1500-1999
		master_list.append(ts[2000:2500])#2000-2499

		master_list.append(ts[250:750]) #250-749
		master_list.append(ts[750:1250]) #750-1249
		master_list.append(ts[1250:1750]) #1250-1749
		master_list.append(ts[1750:2250]) #1750-2249

		for i in master_list:
			n=normalise(i)
			ls = convert_s(n,window_size,number_of_bands,max_value)
			letter_list_agg = letter_list_agg + ls
		
		#============ Changes ===============**************
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


	print(data_size)
	print(unique_size)

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
	
	
	alphabet2=conversion(alphabet)
	alphabet2.sort()
	
	with open('output_latest.pickle', 'wb') as handle:
  		pickle.dump(alphabet2, handle) # watch out here

	print('\n')


	
	print(alphabet2)

	
	print('-----------  n = %d, k = %d, Max = %d -------------' % (window_size, number_of_bands, max_value))

	print('\n')
	
	print('Running Time (s): %f' %time)
	print ('Sample size: %d' %data_size)



#print('---- String Version 50 new ----')

#stock_list = list(range(0,10)) #1168
#main(stock_list,5, 50, 100)



'''
2 year max-min

-----------  n = 5, k = 50, Max = 100 -------------

Running Time (s): 52910.675024
Sample size: 5213952

'''
def alphabet_info(file_name):
	with open(file_name, 'rb') as handle:
		a = pickle.load(handle)

	a.sort()
	#print(a)
	non_zero = len(a)
	entropy = calculate_entropy(a)
	ordered_a = sorted(a, key=lambda tup: tup[1], reverse=True)

	print ('Number of Non-Zero : %d' %non_zero)
	print ("Entropy: %f" %entropy) 
	print('Top X:')
	print(ordered_a[0:10])

	

alphabet_info('./data/alphabet2.pickle')



