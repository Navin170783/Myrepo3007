def f2(n):
    if n<1:
        return 1
    else:
        return f2(n-1) + f2(n-2)
n2=int(input("Enter a Number"))
print(" fibnacci::\n",f2(n2))