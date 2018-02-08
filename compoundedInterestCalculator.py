#interest calculator

def annualInterest(principal, interestPercentage):
    interestAmount=(principal*interestPercentage)/100
    return interestAmount

def compoundedYearlyInterest(principal, interestPercentage, years):
    interest = 0
   # p = principal
    for i in range(years):
        principal = principal + annualInterest(principal,interestPercentage)

   # print ('Return on', p,'at the end of',years,'years is', principal)
    return principal

def compoundedInterest(p,i,y,t):

    if t=='q':
        print ('quaterly compounded')
        q= y*4

        for x in range (q):
            p = p + (annualInterest(p,i)/4)

        print (p)
        
    elif t=='h':
        print ('half yearly compounded')
        h= y*2

        for x in range (h):
            p = p + (annualInterest(p,i)/2)

        print (p)
        
    elif t=='m':
        print ('monthly compounded')
        m= y*12

        for x in range (m):
            p = p + (annualInterest(p,i)/12)

        print (p)
        
    elif t=='a':
        print ('yearly compounded')
        print (compoundedYearlyInterest(p,i,y))


p = float(input('Please enter principal amount:'))
i = float(input('Please enter annual compounded interest rate:'))
y = int(input('For how many number of Years you want to calculate:'))
t= input('Select letter for different types of compounding interest \n'\
         ' m - monthly\n q - quarterly \n h - for half yearly\n a- annually\n:')

compoundedInterest(p,i,y,t)
