N = 20



#Calculate all the primes smaller than N
n = 3
primes=[2]
while n <= N:
	for prime in primes:
		if n%prime == 0:
			break
	else:
		primes.append(n)
	n += 2

LCM = 1 #initialize the least common multiple
for n in range(1, N+1):
	if LCM%n != 0:
		for prime in primes:
			if (LCM*prime)%n == 0:
				LCM *= prime
				break

print(LCM)