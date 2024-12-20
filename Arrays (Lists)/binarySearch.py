def binarySearch(arr,s,e,k):
    if s<=e:
        mid = (s+e)//2
        if arr[mid] < k:
            return binarySearch(arr, mid+1, e, k)
        elif arr[mid] > k:
            return binarySearch(arr, s, mid-1, k)
        else:
            return mid
    else:
        return -1

li = list(map(int, input().split()))
pos = binarySearch(li, 0, len(li), 1)
if pos!=1 :
    print("Element is present at " + str(pos))
else:
    print("Not present")
            
