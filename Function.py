#Simple function

'''def max1(a,b):
    if(a>b):
        print(a,'is greater then',b)
    else:
        print(b,'is greater then',a)
  
f,k =input("Enter two number to check which number is greater :- ").split()  
max1(f,k)'''




#Function with return value

'''def absolute_value (n):
    if(n>=0):
        return(n)
    else:
        return (-n)

num=int (input('Enter a number :- '))
print(absolute_value(num))'''



#Actual and formal parameter

'''def AFP (x,y):
    x=x+2
    y=y+4
    print('Value of x and y inside the function is',x,'and',y)
x,y=10,7
AFP(x,y)
print('Value of x and y outside the function is',x,'and',y)'''




#Type of function arguments

# (1) Python positional arguments

'''def attach(s1,s2):
    s3=s1+s2
    print(s3)
attach('Hello ','world ')
#attach('Hello') generate an error'''

# (2)Python default arguments

'''def greet(name, msg='Good morning'):
    print('Hello',name,msg)
greet('Mohaseen Ali')
greet('Mohaseen Ali','How do you do')'''


'''def greet(msg='Good morning' ,name):
    print('Hello',name,msg)
greet('Mohaseen Ali')'''
#greet('How do you do','Mohaseen Ali') it will generate an error

# (3)Python Keyword arguments

'''def greet(name, msg='Good morning'):
    print('Hello',name,msg)
greet(name = 'Mohaseen Ali',msg = 'How do you do')
greet(msg = 'How do you do', name = 'Mohaseen Ali')
greet('Mohaseen Ali', msg = 'How do you do')'''
#greet(msg = 'How do you do', 'Mohaseen Ali') given an error

# (4)Python arbitary argumnets

'''def greet(*name):
    for name in name:
        print('Hello',name)
greet('Medu','Abbas','Zahid','Abbachi')'''




# Scope of a variable in function

# Local Variable

'''var=100
def fun():
    var=10
    print('Local variable = ',var)
print('Global variable = ',var)
fun()
print('Global variable = ',var)'''

# Global Variable

'''var=45
def fun():
    global var # 2nd does not generates an error due too this
    var=var+34 #it generates an error
    print('Var = ',var)
fun()'''




# Specificaton of function

# Docstring

'''var=45
def fun():
    """This will not give an error of global variable"""#This is a Docstring
    global var # 2nd does not generates an error due too this
    var=var+34 #it generates an error
    print('Var = ',var)
fun()
help(fun)'''




# System function And Parameters

import sys
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

def main(arg):
    print(arg)

main(sys.argv[0])
main("Medyoooo")