import random
n = 10
lowerLimit = -100
upperLimit = 100
arr = []
for i in range(1, n + 1):
    arr.append(random.randint(lowerLimit, upperLimit))
#print(arr)

def findMaxSumCrossArray(low, mid, high, arr):
    maxLeftIndex = mid
    maxLeftSum = arr[mid]
    sumLeftArray = 0
    for i in reversed(range(low, mid + 1)):
        sumLeftArray = sumLeftArray + arr[i]
        if sumLeftArray > maxLeftSum:
            maxLeftSum = sumLeftArray
            maxLeftIndex = i
    maxRightIndex = mid + 1
    maxRightSum = arr[mid + 1]
    sumRightArray = 0
    for i in range(mid + 1, high + 1):
        sumRightArray = sumRightArray + arr[i]
        if sumRightArray > maxRightSum:
            maxRightSum = sumRightArray
            maxRightIndex = i
    return (maxLeftIndex, maxRightIndex, maxLeftSum + maxRightSum)


    
def findMaxSubarray(low, high, arr):
    if low == high:
        return (low, high, arr[low])
    else:
        mid = int((low + high) / 2)
        (leftMaxIndexL, leftMaxIndexR, leftSum) = findMaxSubarray(low, mid, arr)
        (rightMaxIndexL, rightMaxIndexR, rightSum) = findMaxSubarray(mid + 1, high, arr)
        (crossMaxIndexL, crossMaxIndexR, crossSum) = findMaxSumCrossArray(low, mid, high, arr)
        if leftSum > rightSum and leftSum > crossSum:
            return (leftMaxIndexL, leftMaxIndexR, leftSum)
        elif rightSum > leftSum and rightSum > crossSum:
            return (rightMaxIndexL, rightMaxIndexR, rightSum)
        else:
            return (crossMaxIndexL, crossMaxIndexR, crossSum)


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(arr)
print(findMaxSubarray(0, len(arr) - 1, arr))
