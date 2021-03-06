# 
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
#

def fib(max):
	''' Fibonacci generator
	'''

	a, b = 0, 1

	while a < max:
		yield a
		a, b = b, a + b

# Do it
result = 0
for n in fib(4000000):
	if (n % 2 == 0):
		result += n

print(result)
	