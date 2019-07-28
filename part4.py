# Part 4 of the Python Review
def is_prime(x):
	for i in range(2,x-1):
		if x%i == 0:
			return False
	return True
class Cipher:

	def __init__(self, secret_message, key, limit):
		self.secret_message = secret_message
		self.key = key
		self.limit = 10000
		if self.key <=1 or self.secret_message<=1:
			print("Invalid input: Keys and messages must be greater than one.")
		if is_prime(self.key) == false or is_prime(self.secret_message) == false:
			print("Invalid input: Both key and message must be prime.")
		if self.key > self.limit or self.key >self.limit:
			print("Invalid input: Keys and messages must be at most the limit, which is <LIMIT>.")

		
	def encode(self):
		self.coded_message = self.key * self.secret_message


class Decoder:

	def __init__(self, coded_message, limit):
		self.coded_message = coded_message
		self.limit = limit


	def decode(self):
		for i in range(2,limit):
			for k in range(2,limit):
				if j*k == coded_message:
					return (j,k)
		
