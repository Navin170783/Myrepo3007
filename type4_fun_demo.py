def f1(food):
    return food

def f2():
    l2=[]
    l=[1,2,3,4,5,6]
    l2=f1(l)
    for x in l2:
        print(x)
    t1=(10,20,30,40)
    t3=(f1(t1))
    print(t3)
    s={"app","app1","app3"}
    s2=f1(s)
    print(s2)

f2()