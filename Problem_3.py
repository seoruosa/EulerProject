import os.path

NUM = 600851475143
FileName = 'listOfPrimes.txt'
# Program that prints primes smaller than MAX

MAX = int(NUM**0.5)

primes = []
if os.path.isfile(FileName):
	with open(FileName, 'r') as f:
		for line in f:
			primes.append(int(line))
else:
	with open(FileName, 'w') as f:
		f.write('2\n3')
		primes.append(2)
		primes.append(3)

with open(FileName, 'a') as f:
	MAXPRIME = primes[-1]
	n = MAXPRIME
	while n <= MAX:
		for prime in primes:
			if n%prime == 0:
				break
		else:
			if n > MAXPRIME:
				primes.append(n)
				f.write(str(n) + '\n')
			if NUM%n == 0:
				MAX = NUM/n
				print('MAX: %d\n' % MAX)
			print(n)
		n += 2

lpf = 0
for prime in primes:
	if NUM%prime == 0:
		lpf = prime
		print(prime)

with open(FileName,'w') as f:
	for prime in primes:
		f.write(str(prime)+'\n')

print('The largest prime factor is: ' + str(lpf))