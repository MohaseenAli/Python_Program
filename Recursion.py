'''i=0
def greet():
    global i
    i=i+1
    print('Hello ,',i)
    greet()
greet()'''

'''def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

n= int(input('Enter number to find its factorial :- '))
a=fac(n)
print('Factorial of',n,'is ',a)'''

'''def square(n):
    return n*n
result=square(5)
print(result)'''

# LAMBDA Function
'''square=lambda x:x*x
add=lambda a,b:a+b
max=lambda x,y: x if x>y else y
result=square(6)
result1=add(5,23)
result2=max(5,23)
print(result)
print(result1)
print(result2)'''

#FILTER function
'''def fun(variable):
    vowels=['a','e','i','o','u']
    if variable in vowels:
        return True
    else:
        return False
n1=fun('g')
n2=fun('u')
print(n1)
print(n2)


#Sequence

sequence=['g','e','e','j','k','o','p','r']
filtered=filter(fun,sequence)
print('The filtered letter are')
for s in filtered:
    print(s) '''

'''seq=[1,2,3,4,5,6,7]
even =list(filter(lambda x:x%2==0,seq))
print (even)'''

# MAP
# difference between Filter and Map

seq=[1,2,3,4,5,6,7]
square=list(map(lambda x:x*x,seq))
sq=list(filter(lambda x:x*x,seq))
sq1=list(filter(lambda x:x%2==0,seq))
print (square)
print (sq)
print (sq1)

#Reduce

'''lst=[1,2,3,4,5,6,7]
result=reduse(lambda x,y:x*y,lst)
print(result)'''