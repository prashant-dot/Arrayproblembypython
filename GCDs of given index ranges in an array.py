a=[2, 3, 60, 90, 50]
qs=0
qe=2
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
g=gcd(a[qs],a[qs+1])
qs+=2
while qs<=qe:
    g=gcd(g,a[qs])
    qs=qs+1
print(g)

==>O(n*log(min(a,b)))
