class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def __str__(self):
	
		# Defining a blank res variable
		res = ""
		
		# Initializing ptr to head
		ptr = self.head
		
		while ptr:
			res += str(ptr.val) + ", "
			ptr = ptr.next

	# Removing trailing commas
		res = res.strip(", ")
		
		if len(res):
			return "[" + res + "]"
		else:
			return "[]"


if __name__ == "__main__":

	# Defining a linked list
	ll = LinkedList()

	# defining nodes
	node1 = Node(10)
	node2 = Node(15)
	node3 = Node(20)

	# Connecting the nodes
	ll.head = node1
	node1.next = node2
	node2.next = node3
	print(ll)

#Output:-[10,15,20]
