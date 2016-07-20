import pickle


def spliting(a_string):
	a = a_string[:-1] 
	b = a.split(',')
	c = tuple([int(x) for x in b])
	return c


'''
print(spliting ('100,1,2,4,5,'))

print(spliting ('3,2,3,4,6,'))
'''




def conversion (alphabet_s):
	new_alphabet = [] 
	for item in alphabet_s:
		x = (spliting(item[0]),item[1])
		new_alphabet.append(x)
	return new_alphabet






def run_conversion():
	with open('output_new.pickle', 'rb') as handle:
  		alphabet_s = pickle.load(handle)

	a = conversion(alphabet_s)

	with open('output2.pickle', 'wb') as handle2:
  		pickle.dump(a, handle2)

run_conversion()