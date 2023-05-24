#Power of a to b using recursion
def power(a, b):
    #Base condition
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

print(power(2,5))

#Factorial of a number 
def factorial(x):
    if (x==0 or x==1):
        return 1
    else:
        return x*factorial(x-1)
        
a = int(input("Enter your number:"))
print(factorial(a))

#Printing nth term of fibonacci sequence
def fibo(num):
    #Base case 
    if(num == 0):
        return 0
    if(num == 1):
        return 1
    else:
        return fibo(num-1) + fibo(num-2)
        #Gives u the number present on the nth term
print(fibo(10))

