sum_35 = 0

for i in range(1,1000):
	sum_35 += i if (i%3==0 or i%5==0) else 0
	print(sum_35)

