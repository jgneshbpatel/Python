#FileName: PrimeNumbers.py

#Defining function to get prime numbers till provided number

def func(n):
    
    primeNumbers=[]
    for x in range(n+1):
        i=1
        count = 0
        while i<=x:
            if x%i==0:
                #print ('x is:', x)
                #print ('i is:', i)
                count = count + 1
                i=i+1
            else:
                i = i+1

        if count==2:
            primeNumbers.append(x)
            #print ('prime number:', x)

    print (primeNumbers)
               
#calling function

p = int(input('Enter Number to get prime numbers till that number:'))
func(p)
            
