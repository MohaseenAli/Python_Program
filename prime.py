# To print all the prime number between an given interval

'''Lower_bound = int (input('Enter lower bound :- '))
Upper_bound = int (input('Enter upper bound :- '))
for number in range(Lower_bound,Upper_bound+1):
    if (number>1):
        for i in range(2,number):
            if(number%i==0):
                break
        else:
            print(number)'''


#To check a given number is prime not 

number= int(input("Enter a number to check weather it is prime or not :- "))
if (number>1):
    for i in range(2,number):
        if(number%i==0):
            print(number,' is not a prime number')
            break
    else:
        print(number,' is a prime number')
else:
    print(number,' is not a prime number')