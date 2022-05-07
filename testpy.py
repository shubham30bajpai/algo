def funConvertListToDict(lst, dct):
	for i in lst:
		if i in dct:
			dct[i] += 1
		else:
			dct[i] = 1
	

lst = [3,1,2,3,6,4,5]
k = 8
dct = {}
funConvertListToDict(lst, dct)
print(dct)

dctkeys = list(dct.keys())
#i = 0
#j = len(dctKeys) - 1

def funFindPairs(i, j, dctkeys, k):
	print(i, j)
	while i < j:
		if dctkeys[i] + dctkeys[j] == k:
			print(dctkeys[i], dctkeys[j])
			funFindPairs(i + 1, j, dctkeys, k)
			funFindPairs(i, j - 1, dctkeys, k)
		elif dctkeys[i] + dctkeys[j] < k:
			i = i + 1
		else:
			j = j - 1

funFindPairs(0, len(dctkeys) - 1, dctkeys, k)
