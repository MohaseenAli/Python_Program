#x=10
#y=5
x,y=10,5
print('\nadd')
print(x+y)
print('\nsub')
print(x-y)
print('\nmul')
print(x*y)
print('\nmod')
print(x%y)
print(10%3)
print('\ndiv')
print(5/3)
print(5//3)
print('\nexpo')
print(5**3)
print('\nx>y is',x>y)
print('\nx<y is',x<y)
print('\nx=y is',x==y)
print('\nx not equal to y is',x!=y)
x=True
y=False
print('\nAND operators\n',x and y)
print('\nOR operators\n',x or y)
print('\nNOT operators\n',not y)
x=5
y=5
print('\n',id(x))
print(id(y))
print(x is y,'\n')
x=5
y=6
print(id(x))
print(id(y))
print(x is y,'\n')
x=5
y=5
print('\n',id(x))
print(id(y))
print(x is not y,'\n')
x=5
y=6
print(id(x))
print(id(y))
print(x is not y,'\n')
s1=[1,2,3,4,5]
s2=[1,2,3,4,5]
print(s1 is s2)
print(s1 is not s2)
print(1 in  s2)
x='hello'
print('\n','h' in x)
dict={1:"A",2:"b"}
print('\n',1 in dict)
print(3 in dict)
print('\n',10>>1)#10: 1010>>1 ==> 0101
print(10<<1)#10: 1010<<1 ==> 10100

