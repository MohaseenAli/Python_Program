'''str='Mohaseen Ali'
print('\n',str)
str1="""This is my multiline
 string
 ...str1...."""
print('\n',str1)'''

'''str='Mohaseen Ali'
print('\n',str[3],'\n')
for i in range(12):
    print(str[i])
print('\n')
for ch in str:
    print(ch)'''

#Negative indexing
'''print('\nNegative Index\n')
print(str[-1])
print(str[-12])
print(str[-6],'\n')
for i in range(-12,0,1):
    print(str[i])'''



#=============>STRING IS IMMUTABLE<===============

# *******STRING OPERATORS*********

'''str='Mohaseen '
str1='Ali'''

# (1) Concatenation
'''print(str+str1)'''

# (2) Repetiton
'''print(str*4)'''

# (3) Slice[]
'''print(str[3])
print(str[5])
print(str[-5])
print(str[-7])'''

# (4) Range Slicing[ start : stop : step size/jump]
'''str='Mohaseen Ali Thavra'
print(str[9:12])
print(str[0:19:2])
print(str[1:19:2])
print(str[0:19:4])
print(str[::-1])''' #Print string in reverse order 

# (5) Membership in and not in

'''str='Mohaseen Ali'
print('y' in str)
print('a' in str)
print('A' in str)
print('m' in str)
print('m' not in str)
print('M' in str)'''

#  ******STRING FUNCTION******

'''str='moHAsEeN AlI' '''

# Count

'''str1='emoeeHeeAsEeN AelIee'
print(str1.count('e'))'''

# Length of string
'''print(len(str))'''

# Capitalize first letter of string
'''print(str.capitalize())'''

#LowerCase 
'''print(str.lower())'''

#UpperCase
'''print(str.upper())'''

#Returns string with swaped case (it will swap lower too upper and upper to lower case)
'''print('HeLlO WoRlD'.swapcase())'''

#To check that the given string consist only digit or not
'''str='Mohaseen'
str1='A3li'
str2='2134234'
print(str.isdigit())
print(str1.isdigit())
print(str2.isdigit())'''

#To check that the whole string is in upper case or not 

'''str='MOHASEEN ALI'
str1='mohaseen ali'
print(str.isupper())
print(str1.isupper())'''

#To check length of string 

'''str='Mohaseen Ali'
print(len(str))
print(len('Hello World'))'''

# find & replace

'''str = 'Mohaseen Ali'
print(str.find('en'))
print(str.replace('Ali','Ali Thavra'))'''

#Remove whiteSpace
'''print('  hello    '.lstrip())
print('  hello  v  '.rstrip())
print('  hello  v  '.strip())'''

#split function
'''print('Mohaseen Ali Mohammed Ali Kazim Ali Thavra'.split())
print('Mohaseen,Ali,Mohammed,Ali,Kazim,Ali,Thavra'.split(','))'''

#join function

print(' '.join(['Mohaseen','Ali','Mohammed','Ali','Kazim','Ali','Thavra']))