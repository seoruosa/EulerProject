biggestPal, ib, jb = (0, 0, 0)


for i in range(1000,100,-1):
	for j in range(1000,100,-1):
		if (i*j == int(str(i*j)[::-1])):
			print('%d * %d = %d' % (i, j, i*j))
			if i*j > biggestPal:
				biggestPal, ib, jb = (i*j, i, j)

print("The biggest palindrome is: %d * %d = %d " % (ib, jb, biggestPal))