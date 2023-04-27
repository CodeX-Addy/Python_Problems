#Python program to give next prime number to a given number
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

# Example usage
print(next_prime(2100290130013)) 
#Output : 2100290130073
