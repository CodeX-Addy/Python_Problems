class Stack:

	def __init__(self):
		self.Elements = []
		
	def push(self, value):
		self.Elements.append(value)
	
	def pop(self):
		return self.Elements.pop()
	
	# empty() check the stack is empty of not
	def empty(self):
		return self.Elements == []
	
	# show() display stack
	def show(self):
		for value in reversed(self.Elements):
			print(value)

def BottomInsert(s, value):

	# check the stack is empty or not
	if s.empty():
		
		# if stack is empty then call
		# push() method.
		s.push(value)
		
	# if stack is not empty then execute
	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)

# Reverse() reversing the stack
def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)


stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()
