list1=[2,5,8,10]
list2=[3,5,4,9,]

list3=[]
for i in range(0,len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)