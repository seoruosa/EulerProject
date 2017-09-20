N = 100

ans = 0
for i in range(1, N+1):
	for j in range(1, N+1):
		if i!= j:
			ans += i*j

print('Answer: %d' % ans)