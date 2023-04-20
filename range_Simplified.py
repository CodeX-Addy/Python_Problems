sum = 0
for i in range(1,21,2): #This will return the sum of numbers from 0 to 20 which is not divisible by 0,2or5
    if(i%3!=0 and i%5!=0):
        # print(i)
        sum+=i
print(sum)
