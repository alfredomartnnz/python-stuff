#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
#if statement: if variable x is <50 print ('statement')
#else statement: if variable x is >50 print ('statement')
#elif statement: if variable x is ==50 print ('statement')
#int statement: integer must be number
#input statement: 
x = int(input("enter amount: "))

if x<50:
    print('your number is less than 50')
    print('your number is: ',x)
elif x==50:
    print('your number is equal to 50')
    print('the number you type was: ',x)
else:
    print('your number is greater than 50')
    print('your number is: ',x)
