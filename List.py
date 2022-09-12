list1=[2,5,8,10]
list2=[3,5,4,9,]
print("list1=",list1)
print("list2=",list2)
list3=[]
for i in range(0,len(list1)):
    list3.append(list1[i]+list2[i])
print("Sum of list=",list3)