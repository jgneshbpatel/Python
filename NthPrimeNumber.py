#FileName: PrimeNumbers.py

#Defining function to get prime numbers till provided number

def func(n):
    
    primeNumber=0
    x=2
    while primeNumber<n:
        i=1
        count = 0
        while i<=x:
            if x%i==0:
                count = count + 1
                i=i+1
            else:
                i = i+1
                
        if count==2:
            x = x+1
            primeNumber = primeNumber + 1
        else:
            x=x+1
            
    if primeNumber==n:
        print ('Nth prime number: ', x-1)
    else:
        print ('Nth prime number is not found. Try again')



p = int(input('Enter Nth prime number you want to know:'))
func(p)
