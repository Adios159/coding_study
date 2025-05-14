numList = [0, 0, 0, 0]
for i in range(0, 4):
    numList.append(0)
hap = 0

for i in range(0, 4):
    numList[i] = int(input())

for i in range (len(numList)):
    hap += numList[i]

print(hap)