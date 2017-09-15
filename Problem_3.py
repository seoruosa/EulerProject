NUM = 600851475143

# Program that prints primes smaller than MAX

MAX = int(NUM**0.5)
n=3
primes=[2]
while n <= MAX:
	for prime in primes:
		if n%prime == 0:
			break
	else:
		primes.append(n)
		if NUM%n == 0:
			MAX = NUM/n
			print('\n')
		print(n)
	n += 2

print('\n\n\n\n')
#lpf = 0
for prime in primes:
	if NUM%prime == 0:
		lpf = prime
		print(prime)

print('The largest prime factor is: ' + str(lpf))