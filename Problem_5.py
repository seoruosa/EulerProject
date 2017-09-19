N = 10

SCDlist = []
for i in range(1,N+1):
	SCDlist += [i]

n = 3
primes=[2]
while n <= N:
	for prime in primes:
		if n%prime == 0:
			break
	else:
		primes.append(n)
	n += 2

SCD=[]
for prime in primes:
	SCD.append(prime)

print(SCD)