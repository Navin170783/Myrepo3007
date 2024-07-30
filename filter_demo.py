numbers_=[1,2,3,4,5,6]
even_List=list(filter(lambda num:num%2==0,numbers_))
odd_List=list(filter(lambda num:num%2!=0,numbers_))
print("Even List \n",even_List)
print("odd List \n",odd_List)
d1=[34,34,34]
stu_status=list(filter(lambda s:s<35, d1))
if stu_status==True:
    stu_status="Pass"
else:
    stu_status="fail"
print(stu_status)