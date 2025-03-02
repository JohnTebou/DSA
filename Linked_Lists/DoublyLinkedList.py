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
		if not self._length:
			return Exception("list is empty")
		if self.head.value == value:
			return self.pop_left()
		current_node = self.head
		while current_node is not None and current_node.value != value:
			current_node = current_node.next
		if current_node is None:
			return Exception("value not found")
		elif current_node.next is None:
			return self.pop_right()
		else:
			current_node.previous.next = current_node.next
			current_node.next.previous = current_node.previous
			current_node.next = current_node.previous = None
		self._length -= 1
		return current_node.value

	def reverse(self):
		if self._length <= 1:
			return self
		curr = self.head
		while curr != None:
			curr.next, curr.previous = curr.previous, curr.next
			curr = curr.previous
		self.head, self.tail = self.tail, self.head
		return self
	
	def valuelist(self):
		if not self._length:
			return []
		if self._length == 1:
			return [self.head.value]
		curr = self.head
		value_list = []
		while curr != None:
			value_list.append(curr.value)
			curr = curr.next
		return value_list
	
my_list = DoublyLinkedList()
empty_list = DoublyLinkedList()
one_element_list = DoublyLinkedList().append(1)

order_list = DoublyLinkedList()
order_list.append(1)
order_list.append(2)
order_list.append(3)
order_list.append(4)
order_list.append(5)
order_list.append(6)

order_list.remove(4)

print("ordered without 4:", order_list.valuelist())

order_list.reverse()

print("reverse previous:", order_list.valuelist())