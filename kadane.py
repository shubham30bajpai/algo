def funConvertListToDict(lst, dct):
	for i in lst:
		if i in dct:
			dct[i] += 1
		else:
			dct[i] = 1
	

lst = [1,2,3,3,4,5,6]
lst.sort()
k = 8
dct = {}
funConvertListToDict(lst, dct)
print(lst)

dctkeys = list(dct.keys())
#i = 0
#j = len(dctKeys) - 1

def funFindPairs(i, j, dctkeys, k):
    print(i, j)
    while i < j:
        if dctkeys[i] + dctkeys[j] == k:
            print('match', i, j)
            funFindPairs(i + 1, j, dctkeys, k)
            print('second')
            funFindPairs(i, j - 1, dctkeys, k)
            break
        elif dctkeys[i] + dctkeys[j] < k:
            i = i + 1
        else:
            j = j - 1

funFindPairs(0, len(lst) - 1, lst, k)
