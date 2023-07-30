str1 = "Python=10,AI=20, ML=30"
lst=[]
for x in str1.split(','):
    print(x)
    y=x.split('=')
    print(y)
    lst.append(y)
    print(lst)
print(lst)
d=dict(lst)
print(d,'\n\n')

d1={}
d1.fromkeys(['Math','English','Science'], 0)
print(d1,'\n\n')

squares = {1: 10, 2: 24, 's': 25, 'k': 49}
print(squares.items())
print(squares.keys())
print(squares.values())
del(squares[2])
print(squares)
print(1 in squares)
print('s' in squares)
print(25 in squares,'\n\n')

d={1:'Python',2:'Java'}
d.clear()
print (d,'\n\n')

marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks)))
print(list(sorted(marks.values())))
print(list(sorted(marks.keys())))
print('\n\n')

d={1:'Python',2:'Java'}
d[10]="Bye"
print (d.get(1,'none'))
print (d.get(3,'Key not exist'))
print(d.get(10,'Ket not exist'))
print('\n\n')


d={1:'Python',2:'Java',3:'AI'}
print (d.pop(1,'Not Present'))
print(d)
print (d.pop(30,'Not Present'))
print(d,'\n\n')


d={1:'Python',2:'Java',3:'AI'}
print(d.popitem())
print(d,'\n\n')


d={1:'Python',2:'Java'}
print (d.setdefault(2,0))
print(d.setdefault(1,'ADA'))
print (d.setdefault(3,'AI'))
print('\n\n')


d={1:'Python',2:'Java',3:'AI'}
ud={3:'ML',4:'AI'}
d.update(ud)
print (d)
d.update({5:'AI++'})
print (d)
d.update({5:'C++'})
print (d,'\n\n')