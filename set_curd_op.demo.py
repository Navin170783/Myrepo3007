s1={"apple"}
for x in range(10):
    print("1.adding element”)
    Print("2.delete given element”)
    Print("3.displayelements”)
    Print("4.update the given element”)
    Print("5.unknown op”)
    print("6.search the given element")
    n1=input("enter your choice”)
    match n1:
    case “1”:  
            ele=input(“enter ele”)
            s1.add(ele)
    case “2”:
            ele2=input(“enter ele for delete”)
            s1.remove(ele)
    case”3”:
            For in in s1
            print(i)
    case “4”:
            l1=list(s1)
            n1=int(input(“enter a index for updating ele”))
            Upele=input(“enter a update ele”)
            l1=[n1]=upele
            s1=set(l1)
    case "5":
            exit(0)
    case "6":
            s4=input("enter a searching ele")

            for x1 in s1:
                if x1==s4:
                    c=c=1
                else:
                    c=0
                if  c==1:
                    print("ele is found")
 

