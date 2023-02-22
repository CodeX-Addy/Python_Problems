def palindrome(a):
   mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign 
    start = 0                #so that you can compare the middle elements also.
    last = len(a)-1
    flag = 0
 
    # A loop till the mid of the
    # string
    while(start <= mid):
  
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
