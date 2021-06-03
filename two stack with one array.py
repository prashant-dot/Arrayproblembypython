class Stack:
    def __init__(self,n):
        self.size1=n//2
        self.size2=n
        self.s=[]
        self.top1=-1
        self.top2=n//2-1
    def push1(self,x):
        if self.top1==self.size1-1:
            print("Overflow")
        else:
            self.top1+=1
            self.s.append(x)
    def pop1(self):
        if self.top1<=-1:
            print("Underflow")
        else:
            x=self.s.pop()
            print(x," is deleted")
            self.top1-=1

    def push2(self, x):
        if self.top2 == self.size2 - 1:
            print("Overflow")
        else:
            self.top2 += 1
            self.s.append(x)

    def pop2(self):
        if self.top2 <= self.size1-1:
            print("Underflow")
        else:
            x = self.s.pop()
            print(x, " is deleted")
            self.top2 -= 1

    def printstack1(self):
        temp=self.top1
        while(temp>=0):
            print(self.s[temp])
            temp-=1
        print()


    def printstack2(self):
        temp = self.top2
        while (temp >= self.size1):
            print(self.s[temp])
            temp -= 1
        print()



st=Stack(5)
st.push1(3)
st.push1(34)
st.printstack1()
st.push2(32342)
st.push2(34124)
st.printstack2()
st.pop2()
st.printstack2()
