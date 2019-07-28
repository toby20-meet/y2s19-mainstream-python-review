# Part 2 of the Python Review lab.

def is_prime(x):
	for i in range(2,x-1):
		if x%i == 0:
			x+=1
	return x

def encode(x, y):
	x = is_prime(x)
	y = is_prime(y)
	if (1<y and y<250) and (500<x and x<1000):
		return x * y
	print("Invalid input: Outside range.")
	return None

def decode(coded_message):
	for i in range(2,249):
		c = i
		if coded_message%c == 0:
			break
	if coded_message//c * c == coded_message:
		return (c, coded_message/c)
	'''
	for i in range(501,999):
		j = i
		if coded_message%j == 0:
			break
	if c*j == coded_message:
		return (c,j)
	'''

print(decode(encode(501,5)))