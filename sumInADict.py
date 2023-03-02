# Python program to print sum of all items in a dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#Output--> 600
