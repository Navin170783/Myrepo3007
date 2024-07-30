X1=[1,1,"app1","app1",10.8,True,"bye"]
print(type(X1))
print(X1)
for i in X1:
    print(i)
s=int(input("start range"))
n=int(input("ends range"))
for k in range(s,n):
    X1.append(k)
print("after adding dynamic elements",X1)