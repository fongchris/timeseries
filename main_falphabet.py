#exec(open("./data_alphabet.py").read())
#exec(open("./data_fd_x.py").read())
#exec(open("./main_feature.py").read())
from statistics import mean, pstdev
from math import atan, degrees
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
		d1 = (trend_slope(l[0],0.05)+90.0)//1.8 + 1 # = 7
		d2 = (trend_slope(l[0],0.1)+90.0)//1.8 + 1 # = 8 
		d3 = (trend_slope(l[0],0.2)+90.0)//1.8 + 1 # =9 

		l_plus = (l[1],high,low,op,cl,int(mu),int(sd),int(d1),int(d2),int(d3))
		falphabet.append(l_plus)
		done = done+1 
		print(done/loop_size)
	return falphabet



def calculate_entropy (probs):
	entropy = 0
	for p in probs:
		entropy = entropy - p*log(p,2)
	return entropy


def rebalance (probs):
	prob_sum = 0
	new_probs =[]
	for i in alphabet:
		prob_sum = prob_sum+i[1]

	for i in alphabet:
		a = (i[0],i[1]/prob_sum)
		new_alphabet.append(a)
	#print(prob_sum)
	#print(new_alphabet)
	return new_alphabet


def feature_dist(f,falphabet):
	prob_list = []
	done = 0
	for i in list(range(1,101)):
		prob = 0
		for item in falphabet:
			if item[f] == i:
				prob = prob + item[0]
		prob_list.append(prob)
		done = done +1
		sys.stdout.write('\r')
		sys.stdout.write("%f" % (done/100))
		sys.stdout.flush()

	print ('\n')	
	print (prob_list)






def run_falphabet():
	with open('./data/alphabet1.pickle', 'rb') as handle:
		a = pickle.load(handle)
	
	b=distribution_with_features(a)

	with open('./data/falphabet1.pickle', 'wb') as handle2:
  		pickle.dump(b, handle2)


def run_fdist():
	with open('./data/falphabet1.pickle', 'rb') as handle:
  		falphabet = pickle.load(handle)

	feature_dist(6,falphabet)



#run_falphabet()
run_fdist()


