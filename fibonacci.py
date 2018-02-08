# Filename: fibonacci.py

def func(y):
    for i in range(0,y):

        if i<2:
            print (i)
        else:
            i = (i-1) + (i-2)
            print (i)
x = int(input('enter the nth nuber for fibonacci series:'))
func(x)
print ('Done with fibonacci series')
