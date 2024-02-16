in1 = int(input('The first number = \n'))
in2 = int(input('The second number = \n'))

def S_or_M (num1,num2):
    if ( num1 * num2 <= 1000):
        return num1 * num2
    else:
        return num1 + num2
    
result= S_or_M(in1 ,in2)
print('the result is = ',result)