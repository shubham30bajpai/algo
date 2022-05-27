string = 'aaaaaaabcb'
longestString = []
currentString = []
for i in string:
    if i in currentString:
        if len(currentString) > len(longestString):
            longestString = currentString
        currentString = []
        currentString.append(i)
    else:
        currentString.append(i)
        if len(currentString) > len(longestString):
            longestString = currentString

print(longestString)
