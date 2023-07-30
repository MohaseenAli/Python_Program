#number of lines
'''f=open("Text.txt",'r')
l=len(f.readlines())
print('Lines = ',l)'''

#numbers of words

'''f=open("Text.txt",'r')
line=f.read()
word=line.split()
print('words = ',len(word))'''

#numbers of unique words

'''f=open("Text.txt",'r')
line=f.read()
word=set(line.split())
print('words = ',len(word))'''

#number of spaces and character

'''f=open("Text.txt",'r')
line=f.read()
s=0
ch=0
for i in line:
    if(i==' '):
        s+=1
    elif(i=='\n'):
        continue
    else:
        ch+=1
print('space = ',s)
print('character = ',ch)'''

#Read the file and store key in a dictionary and count the frequency of it

f=open("text.txt",'r')
l=list(f.read().lower().split())
d={}
for i in l:
    a=l.count(i)
    d.setdefault(i,a)
print(d)