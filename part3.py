# Part 3 of the Python Review lab.

LETTERS_TO_NUMBERS = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
					  'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
					  'x':23, 'y':24, 'z':25}
NUMBERS_TO_LETTERS = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l',
					  12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w',
					  23: 'x', 24: 'y', 25: 'z'}

def createShiftDictionary(s):
	new_dictionary = {}
	for i in range(0,26):
		new_dictionary[NUMBERS_TO_LETTERS[i]] = NUMBERS_TO_LETTERS[((i+s)%26)]
	#new_dictionary['a'] = NUMBERS_TO_LETTERS[LETTERS_TO_NUMBERS['a']+s]
	return new_dictionary

def encode(plaintext, s):
	cipher = ""
	dicti = createShiftDictionary(s)
	for i in range(0,len(plaintext)):
		if plaintext[i].isalpha():
			cipher += dicti[plaintext[i]]
		else: cipher += plaintext[i]
	return cipher

def decode(ciphertext, s):
	decipher = ""
	dicto = createShiftDictionary(-s)
	for i in range(0,len(ciphertext)):
		if ciphertext[i].isalpha():
			decipher += dicto[ciphertext[i]]
		else: decipher += ciphertext[i]
	return decipher

def decodeAll(ciphertext):
	list_de = []
	for i in range(0,26):
		list_de.append(decode(ciphertext, i))
	return list_de

x = encode("hello, friend.", 4)
print(x)
print(decodeAll(x))