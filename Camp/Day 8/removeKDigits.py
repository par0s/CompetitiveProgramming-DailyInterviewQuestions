def removeK(num,k):
	deck = []
	n = len(num)
	l = n - k

	ans = ""
	for i in range(n):
		if(n - i > l):
			while(deck and deck[-1][0] > num[i]):
				deck.pop()
			deck.append([num[i],i])
			# print(i,deck)
		else:
			while(deck and deck[-1][0] > num[i]):
				deck.pop()
			deck.append([num[i],i])
			ans += str(deck.pop(0)[0])
			# print(i,deck)
			# print("ansChange = ",ans)
	
	res = [i for i in ans]
	while(res and res[0] == "0"):
		res.pop(0)

	res = "".join(res) if res else "0"
	print("#",res)
	return res
	
num = "1432219"
k = 3

# num = "120310"
# k = 2

# num = "10"
# k = 2
removeK(num,k)