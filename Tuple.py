'''x=tuple()
print(type(x))
y=()
print(type(y))

x=(1,4,5,6)
print(x[1])
print(x[-1])
y=(1)
print(type(y))
y=(1,)
print(type(y))'''

'''tup=(1,2,3,x,'Mohaseen','Ali')
print(tup)
print(tup[3])
print(tup[4])
print(tup[3][2])'''

'''student=(1,'Mohaseen Ali',30)
fees=(1500,)
(rno,name,marks)=student
print(rno)
print(name)
print(marks)
r,n=student[0:2]
print(r)
print(n)
print(student+fees)
print(fees*3)
print(1 in student)
print(1500 in student)
print(1500 not in student)
print('Mohaseen Ali' in student)'''

'''tp=(5,3,1,-5,9,1,1,1,0,-2,-8,23,41,-31)
print(len(tp))
print(max(tp))
print(min(tp))
print(tp.index(-2))
print(tp.count(1))
print(sorted(tp))
print(tuple(sorted(tp)))
print(tuple(sorted(tp,reverse=True)))'''

'''x=(1,2,4,5)
print(id(x))
new=(3,)
y=x[0:2]
print(y)
y=y+new
print(y)
x=y+x[2:]
print(x)
print(id(x))'''

'''x=(1,2,6,4,5)
new=(3,)
y=x[0:2]
y=y+new
x=y+x[3:]
print(x)'''

'''x=(1,2,3,6,4,5)
y=x[0:3]
x=y+x[4:]
print(x)'''

'''T=(1,2,3,4)
for i in T:
    print(i)

L=[(1,2),(3,4),(5,6)]
for i in L:
    print(i)

for (x,y) in L:
    print('First',x,'Second',y)

for i in range(len(L)):
    print('Index = ',i,'Element =',L[i])

for i in range(len(T)):
    print('Index = ',i,'Element =',T[i])'''