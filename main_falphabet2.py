from statistics import mean, pstdev
from math import atan, degrees,log
import pickle
import sys


def trend_slope(letter_raw,scale):

	letter = [x*scale for x in letter_raw]
	index_list = list(range(0,len(letter)))
	index_mean = mean(index_list)
	letter_mean = mean(letter)

	upper_sum = 0
	lower_sum = 0
	
	for i in index_list:
		upper_sum = upper_sum +(index_list[i]-index_mean)*(letter[i]-letter_mean)

	for i in index_list:
		lower_sum = (index_list[i]-index_mean)**2

	m = upper_sum/lower_sum
	d = degrees(atan(m))
	return d


def distribution_with_features(alphabet):
	falphabet = []

	loop_size = len(alphabet)
	done = 0
	for l in alphabet:
		high = max(l[0])                   # = 1
		low= min (l[0])						# = 2
		op = l[0][0]						# = 3
		cl = l[0][4]						# = 4
		mu = (mean(l[0])-0.5)//1 +1         # = 5  
		sd = (pstdev(l[0]))//0.5 +1         # = 6
		d1 = (trend_slope(l[0],0.05)+90.0)//3.6 + 1 # = 7
		d2 = (trend_slope(l[0],0.1)+90.0)//3.6 + 1 # = 8 
		d3 = (trend_slope(l[0],0.2)+90.0)//3.6 + 1 # =9 
		d4 = (trend_slope(l[0],0.3)+90.0)//3.6 + 1 # =10 

		l_plus = (l[1],high,low,op,cl,int(mu),int(sd),int(d1),int(d2),int(d3),int(d4))
		falphabet.append(l_plus)
		done = done+1 
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/loop_size))
		sys.stdout.flush()
	return falphabet

def entropy (prob_list):
	entropy = 0.0
	for p in prob_list:
		entropy = entropy - p*log(p,2)
	return entropy


def run_falphabet():
	with open('./data/alphabet2.pickle', 'rb') as handle:
		a = pickle.load(handle)
	
	b=distribution_with_features(a)

	with open('./data/falphabet2.pickle', 'wb') as handle2:
  		pickle.dump(b, handle2)


run_falphabet()





def falphabet_info(file_name):
	with open(file_name, 'rb') as handle:
	  	b = pickle.load(handle)

	print(len(b))
	#e = calculate_fentropy(b)
	#print(e) 
	p_list = [x[0] for x in b]

	print(entropy(p_list))
	ordered_b = sorted(b, key=lambda tup: tup[0], reverse=True)

	print(ordered_b[0:10])

falphabet_info('./data/falphabet2.pickle')

