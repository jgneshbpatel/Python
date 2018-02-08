#interest calculator

def annualInterest(principal, interestPercentage):
    interestAmount=(principal*interestPercentage)/100
    return interestAmount

def compoundedInterest(p,i,y,t):

    months = y*12
    
    if t=='q':

        print ('quaterly compounded')
        
        q=int(months/3)
        
        for x in range (q):
            p = p + (annualInterest(p,i)/4)

        print (p)
        
    elif t=='h':
        
        print ('half yearly compounded')
        
        h= int(months/6)

        for x in range (h):
            p = p + (annualInterest(p,i)/2)

        print (p)
        
    elif t=='m':
        print ('monthly compounded')
        m=int(months)
        for x in range (m):
            p = p + (annualInterest(p,i)/12)

        print (p)
        
    elif t=='a':
        
        h= int(months/12)

        for x in range (h):
            p = p + (annualInterest(p,i))

        print (p)

    else:
        print ('You selected wrong option for compounded interest. Try again')


p = float(input('Please enter principal amount:'))
i = float(input('Please enter annual compounded interest rate:'))
y = float(input('For how many number of Years you want to calculate:'))
t= input('Select letter for different types of compounding interest \n'\
         ' m - monthly\n q - quarterly \n h - for half yearly\n a- annually\n:')

compoundedInterest(p,i,y,t)
