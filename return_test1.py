
from statistics import mean
from math import log
import time
import csv
import timeit




def extract(number):
	ts = []
	with open('1500comma.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			ts.append(row[number])
	del ts[0]
	ts=list(map(float, ts))
	return ts

# ================ simple ================


def simple_return(ts):
	new_ts = []
	last_x = -999 
	for x in ts:
		if last_x == -999:
			last_x = x
		else:
			r = (x/last_x)-1
			new_ts.append(r)
			last_x = x
	#print(new_ts)
	#print(len(new_ts))
	return new_ts


def simple_return_m (ts,factor):
	merged_ts = []
	count=0
	while (count+factor) <= len(ts)-1:
		new_point = log(ts[count+factor]/ts[count])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	#print(len(merged_ts))
	return merged_ts 
#[1,5,20,60,120,240] [day,week,month,quater,half,year]

#simple_return(extract(0))
#simple_return_m(extract(0),240)

# ================ log ================

def log_return(ts):
	new_ts = []
	last_x = -999 
	for x in ts:
		if last_x == -999:
			last_x = x
		else:
			r = log(x/last_x)
			new_ts.append(r)
			last_x = x
	#print(new_ts)
	#print(len(new_ts))
	return new_ts


def log_return_m (ts,factor):
	merged_ts = []
	count=0
	while (count+factor) <= len(ts)-1:
		new_point = log(ts[count+factor]/ts[count])
		merged_ts.append(new_point)
		count = count+factor
	#print(merged_ts)
	#print(len(merged_ts))
	return merged_ts 




def find_max_min():
	start = timeit.default_timer()
	print ('*****  Local Max Min Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = log_return(extract(stock_id)) # simple or log
		ts_aggregated = ts_aggregated + ts1

	stop  = timeit.default_timer()
	print(max(ts_aggregated))
	print(min(ts_aggregated))
	print('Running Time (s): %f' %time)
#find_max_min()
# simple 1.6490066225165565 -0.7266811279826464

def zero():
	print ('*****  Zero Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = simple_return(extract(stock_id))
		ts_aggregated = ts_aggregated + ts1
	print(ts_aggregated.count(0))

#zero()
#32200




def find_global_max_min():
	print ('*****  Global Test  *****')
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for m in [1,5,20,60,120,240]:
		for stock_id in stock_list:
			ts1 = simple_return_m(extract(stock_id),m)
			ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))

#find_global_max_min()
# 11.8113207541698
# 0.960579128


def calculate_band_return (max_value,k,raw_value):
	increment = (max_value+1)/k
	if raw_value == max_value:
		band = k
	else:
		raw_value2 = raw_value+1
		band = int(raw_value2//increment+1)
	print(band)
	return band


calculate_band_return(1.2,1000,0)


