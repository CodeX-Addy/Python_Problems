# Python3 code to demonstrate working of
# Group similar elements into Matrix
# Using list comprehension + groupby()
from itertools import groupby

# initializing list
test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]

# printing original list
print("The original list : " + str(test_list))

# Group similar elements into Matrix
# Using list comprehension + groupby()
res = [list(val) for key, val in groupby(sorted(test_list))]
		
# printing result
print("Matrix after grouping : " + str(res))

#Output-->
# The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2]
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]
