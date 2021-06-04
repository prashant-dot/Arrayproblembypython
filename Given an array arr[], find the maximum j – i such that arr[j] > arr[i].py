n = 9
a = [332, 85, 140, 3, 2, 80, 330, 343, 15]
dic = dict()
for i in range(n):
	if a[i] in dic:
		dic[a[i]].append(i)
	else:
		dic[a[i]] = [i]
a.sort()
maxDiff = 0
temp = n
for i in range(n):
	if temp > dic[a[i]][0]:
		temp = dic[a[i]][0]
	maxDiff = max(maxDiff, dic[a[i]][-1]-temp)

print(maxDiff)
==>O(nlogn)
