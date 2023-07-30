x=10
if x>5:
    print (' \nx is greater then 5')
    print('if ends\n\n')

x,y=10,15
print('x=10 and y=15')
if x>y:
    print('x is greater then y')
else:
    print('x is less then y\n\n')

x=int(input('Enter number :- '))
if x==1:
    print('Monday')
elif x==2:
    print('Tuesday')
elif x==3:
    print('Wednesday')
elif x==4:
    print('Thursday')
elif x==5:
    print('Friday')
elif x==6:
    print('Saturday')
elif x==7:
    print('Sunday')
else:
    print('enter from 1 to 7')

#print('\n\nEnter three number :- ')    
#a=int (input())
#b=int (input())
#c=int (input())
a,b,c = input('\n\nEnter three number :- ').split()
print('\n\na =',a,',b =',b,',c =',c)
if (a>b):
    if (a>c):
        print('\na is greater then b,c')
    else:
        print('\nc is greater then a,b')
else:
    if (b>c):
        print('\nb is greater then a,c')
    else:
        print('\nc is greater then a,b')

m=[7,4,53,645,6,234,55,3]
print('\n\nFirst iteration')
for i in m:
    print(i)
print('\n\nSecond iteration')
s=[4,87,36,0,67]
for i in s:
    print(i)
else:
    print('Second iteration finished')
sum=0
for i in range(10):#i from 0 to 9
    sum+=i
print('\n\nsum=',sum)
print('\n\nLength of m =',len(m))
n=int(input('\n\nEnter number :- '))
sum=0
while(n>0):
    sum+=n
    n-=1
else:
    print('Else of while')
print('sum = ',sum)

print('\n\nbreak at 9 and continue at 2')
for i in range(10):
    if i==2:
        continue
    elif i==9:
        break
    print (i)

print("\n\nIn 'Mohaseen Ali' break at 'l' and continue at 'e'")
for i in 'Mohaseen Ali':
    if i=='e':
        continue
    elif i=='l':
        break
    print (i)

