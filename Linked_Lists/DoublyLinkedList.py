class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._length = 0
	
	def append(self, value):
		new_node = Node(value)
		if not self._length:
			self.head = self.tail = new_node
		else:
			new_node.previous = self.tail
			self.tail.next = new_node
			self.tail = new_node
		self._length += 1
		return self
	
	def prepend(self, value):
		new_node = Node(value)
		if not self._length:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node
		self._length += 1
		return self
	
	def pop_left(self):
		if not self._length:
			return Exception("list is empty")
		former_head = self.head
		if self._length == 1:
			self.tail = self.head = None
		else:
			self.head = former_head.next
			former_head.next = None
			self.head.previous = None
		self._length -= 1
		return former_head.value

	def pop_right(self):
		if not self._length:
			return Exception("list is empty")
		former_tail = self.tail
		if self._length == 1:
			self.tail = self.head = None
		else:
			self.tail = former_tail.previous
			former_tail.previous = None
			self.tail.next = None
		self._length -= 1
		return former_tail.value

	def remove(self, value):
		pass

	def reverse(self):
		pass

	
my_list = DoublyLinkedList()
empty_list = DoublyLinkedList()
one_element_list = DoublyLinkedList().append(1)