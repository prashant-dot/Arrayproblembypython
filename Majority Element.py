a=[4,3,4,4,1,3,4]
n=len(a)
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

if [x for x in dic.values() if x>n//2]:
    print("majority element")
else:
    print("Non majority element")
==> O(n)
