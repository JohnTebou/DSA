class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SinglyLinkedListStack:
	def __init__(self):
		self._top = None
		self._size = 0
		self._max_allowed_size = 10

	def __len__(self):
		return self._size

	# adds an element to stack
	def push(self, value):
		if self._max_allowed_size == self._size:
			raise Exception("stack size limit reached")
		new_node = Node(value)
		new_node.next = self._top
		self._top = new_node
		self._size += 1
		return self
	
	# removes an element from stack
	def pop(self):
		if not self._size:
			return Exception("stack is empty")
		former_top = self._top
		self._top = former_top.next
		former_top.next = None
		self._size -= 1
		return former_top.value
	
	def peek(self):
		return self._top.value if self._top else None
	
	def clear(self):
		self._top = None
		self._size = 0
		return self

	
my_stack = SinglyLinkedListStack()

my_stack.push(1)

print(my_stack._size)

my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print(my_stack.peek())

print(my_stack.pop(), my_stack._size, my_stack.peek())