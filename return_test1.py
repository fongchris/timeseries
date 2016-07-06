
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
	print(new_ts)
	print(len(new_ts))
	return new_ts


def simple_return_m (ts,factor):
	merged_ts = []
	count=0
	while (count+factor) <= len(ts)-1:
		new_point = (ts[count+factor]/ts[count])-1
		merged_ts.append(new_point)
		count = count+factor
	print(merged_ts)
	print(len(merged_ts))
	return merged_ts 
#[1,5,20,60,120,240] [day,week,month,quater,half,year]


#simple_return(extract(0))

simple_return_m(extract(0),240)







def find_max_min():
	stock_list = list(range(0,1168))
	ts_aggregated = []	
	for stock_id in stock_list:
		ts1 = simple_return(extract(stock_id))
		ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))
#find_max_min()
#1.6490066225165565
#-0.7266811279826464



def find_global_max_min():
	stock_list = list(range(0,1168))
	for m in [1,5,20,60,120,240]:
		ts_aggregated = []	
		for stock_id in stock_list:
			ts1 = simple_return_m(extract(stock_id),m)
			ts_aggregated = ts_aggregated + ts1
	print(max(ts_aggregated))
	print(min(ts_aggregated))

find_global_max_min()

