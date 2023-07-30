list1=[]
print(type(list1))
list1=[1,2,3,4]
'''print(list1)'''
list2=['Mohaseen','Ali','Thavra']
'''print(list2)'''
list3=[1,'Mohaseen',3,list2,2,'Ali',3.43,6.78,list1]
'''print(list3)
print(list3[1])
list3[3]=4
print(list3)'''

# List operation

# (1) Range Slice [:]
'''print(list3[2:6])
print(list3[-6:-1])'''

# (2) Concatenation
'''print(list2+list1)
print(list1+list2)'''

# (3) Repetation
'''print(list2*2)
print(2*list2)
print(2*list1*3)
print(['he']*3)'''

# (4) Membership
'''print(3.43 in list3)
print(3.23 in list3)
print(4 in list3)
print(list1 in list3)'''

# List Function
lst1=[1,2,3,8,32]
lst2=[4,5,6,7,9,10]
lst3=[10,11,12]

'''lst1.append(lst2)
print(lst1)'''

'''lst3.extend(lst2)
print(lst3)'''

'''lst2.insert(1,20)
print(lst2)
lst2.insert(4,99)
print(lst2)'''

'''lst2.remove(5)
print(lst2)'''

'''lst2.pop(0)
print(lst2)
lst2.pop()
print(lst2)'''

'''print(lst1)
del lst1[0:3]
print(lst1)'''

'''my_list=[10,32,5,-6,-1,22,0]
lst1=sorted(my_list)
print(lst1)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(max(my_list))
print(min(my_list))
print(sum(my_list))'''

# List iteration

'''for i in lst1:
    print(i)'''

'''l=len(lst1)'''

'''for i in range(l): # OR range(len(lst1))
    print(lst1[i])'''

'''i=0
while(i<l):
    print(lst1[i])
    i+=1'''

'''obj=enumerate(lst1)
print(list(enumerate(lst1)))
for i,val in obj:
    print('index = ',i,'value =',val)'''


'''l=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (l)'''

'''for i in range(3):
    for j in range(4):
        print(i*j,end=' ')
    print('\r')'''