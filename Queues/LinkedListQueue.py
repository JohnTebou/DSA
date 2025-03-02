class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SinglyLinkedListQueue:
	def __init__(self):
		self.head = None
		self.tail = None
		self._size = 0

	# adds an element to queue
	def queue(self, value):
		new_node = Node(value)
		if not self._size:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
		self._size += 1
		return self
	
	# removes an element from queue abiding by FIFO principle
	def pop_left(self):
		if not self._size:
			return Exception("list is empty")
		former_head = self.head
		self.head = former_head.next
		former_head.next = None
		self._size -= 1
		if not self._size:
			self.tail = None
		return former_head.value
	
	# removes all elements from queue
	def clear(self):
		self.head = None
		self.tail = None
		self._size = 0
		return self
	
	# checks first element in queue (first added)
	def peek(self):
		return self.head.value if self.head else None