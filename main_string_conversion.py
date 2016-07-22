import pickle


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


def run_conversion():
	with open('output_a2s50.pickle', 'rb') as handle:
  		alphabet_s = pickle.load(handle)

	a = conversion(alphabet_s)

	with open('alphabet2_50.pickle', 'wb') as handle2:
  		pickle.dump(a, handle2)

run_conversion()

