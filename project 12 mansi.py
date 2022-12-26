n=int(input("n: "))
f=0
s=1
c=0
t=[]
while c<n:
    t.append(f)
    x=f+s
    f=s
    s=x
    c+=1
print(t)
x=int(input("num:"))
y=int(input("num2:"))
if (x in t) and (y in t): 
    print("yes,this is valid")
else:
    print("no, this is not valid")
