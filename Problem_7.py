import os.path

FileName = 'listOfPrimes.txt'

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

print(primes[10000])
