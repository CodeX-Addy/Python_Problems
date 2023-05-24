#Power of a to b using recursion
def power(a, b):
    #Base condition
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

print(power(2,5))
