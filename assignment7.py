#question1

radius= float(input("enter the number:"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)

#end

#question2

n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum=sum+i
    if (sum==n):
        return(True)
    else :
        return(False)
for i in range(1,1001):
    if (perfect(i))==True:
        print(i)

#end


#question3

n=12
def multiplication(n,i=1):
    print(n*i)
    if i!=10:
        multiplication(n,1+i)
print(multiplication(12))

#end

#question4

def power(a,b):
    if (b==1):
        return(a)
    if (b!=1):
        return(a*power(a,b-1))
a=int(input("enter a:"))
b=int(input("enter b:"))
print("result:",power(a,b))

#end

#question5

def factorial(n):
    if(n<=1):
        return 1
    else:
        return(n*factorial(n-1))
d={}
n=int(input("enter number:"))
print("factorial:")
print(factorial(n))
d[n]=factorial(n)
print(d)










