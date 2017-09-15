MAX = 4000000

a = 1
fibo = 1
sumFibo = 0
while fibo < MAX:
	sumFibo += fibo if (fibo%2 == 0) else 0
	n = fibo
	fibo += a
	a = n

print(sumFibo)