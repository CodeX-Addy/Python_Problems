class Node:

	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null
		self.prev = None # Initialize prev as null	
		
class Stack:
	def __init__(self):
		self.head = None
	
	def push(self, data):

		if self.head is None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			self.head.prev = new_node
			new_node.next = self.head
			new_node.prev = None
			self.head = new_node
			
			

	def pop(self):

		if self.head is None:
			return None
		elif self.head.next is None:
			temp = self.head.data
			self.head = None
			return temp
		else:
			temp = self.head.data
			self.head = self.head.next
			self.head.prev = None
			return temp



# Returning top element in the stack
	def top(self):

		return self.head.data


# Returning the size of the stack
	def size(self):

		temp = self.head
		count = 0
		while temp is not None:
			count = count + 1
			temp = temp.next
		return count
	
	
# Function to check if the stack is empty or not
	def isEmpty(self):

		if self.head is None:
		return True
		else:
		return False
			

# Printing the stack
	def printstack(self):
		
		print("stack elements are:")
		temp = self.head
		while temp is not None:
			print(temp.data, end ="->")
			temp = temp.next		
		
		
if __name__=='__main__':

# Starting with the empty stack
stack = Stack()

print("Stack operations using Doubly LinkedList")
stack.push(4)

stack.push(5)

stack.push(6)

stack.push(7)

# Printing the stack
stack.printstack()

# Printing the top element
print("\nTop element is ", stack.top())

# Printing the size of stack
print("Size of the stack is ", stack.size())

# pop the top element
stack.pop()

# pop the top element
stack.pop()

stack.printstack()

print("\nstack is empty:", stack.isEmpty())
