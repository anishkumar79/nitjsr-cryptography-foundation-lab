#question 1:    implement the Euclidean algorithm 


def eucludian(a,b):
    if(a<=0):
     return b
    elif(b<=0):
     return a
    elif (a>b):
     return eucludian(a%b,b)
    return eucludian(a,b%a)

a=int(input("number a:"))
b=int (input("number b:"))


print("gcd(a,b):",eucludian(a,b))