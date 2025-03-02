class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._length = 0

	def append(self, value):
		new_node = Node(value)
		if not self._length:
			self.head = self.tail = new_node
		else:
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
			self.head = new_node
		self._length += 1
		return self
	
	# def pop_left(self):
	# 	if not self._length:
	# 		return self
	# 	else:
	# 		placeholder = Node(0)
	# 		placeholder.next = self.head.next
	# 		del self.head
	# 		self.head = placeholder.next
	# 		del placeholder
	# 	self._length -= 1
	# 	return self

	def pop_left(self):
		if not self._length:
			return Exception("list is empty")
		former_head = self.head
		self.head = former_head.next
		former_head.next = None
		self._length -= 1
		if not self._length:
			self.tail = None
		return former_head.value
	
	def pop_right(self):
		if not self._length:
			return Exception("list is empty")
		tail_value = self.tail.value
		if self._length == 1:
			self.head = self.tail = None
		else:
			temp_node = self.head
			while temp_node.next is not self.tail:
				temp_node = temp_node.next
			self.tail = temp_node
			self.tail.next = None
		self._length -= 1
		return tail_value

	def remove(self, value):
		if not self._length:
			return Exception("list is empty")
		if self.head.value == value:
			return self.pop_left()
		previous_node = self.head
		current_node = self.head.next
		while current_node is not None and current_node.value != value:
			previous_node = current_node
			current_node = current_node.next
		if current_node is None:
			return Exception("value not found")
		elif current_node.next is None:
			self.tail = previous_node
			previous_node.next = None
		else:
			previous_node.next = current_node.next
			current_node.next = None
		self._length -= 1
		return current_node.value
	
	def reverse(self):
		if self._length <= 1:
			return self
		prev = None
		curr = self.head
		while curr != None:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
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


my_list = SinglyLinkedList()
empty_list = SinglyLinkedList()
one_element_list = SinglyLinkedList().append(1)

# print(my_list)
# print(my_list.head)
# print(my_list.tail)
# print(my_list._length)

# my_list.append(3)
# my_list.append(5)
# my_list.append(7)

# print(my_list)
# print("head value:", my_list.head.value)
# print("tail value:", my_list.tail.value)
# print("list length:", my_list._length)

# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.prepend(2)

# print("list head:", my_list.head.value)
# print("list length:", my_list._length)

# print("value to pop from left:", my_list.pop_left())
# print("list head:", my_list.head.value)
# print("list length:", my_list._length)

# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.prepend(2)

# print("value to pop from right:", my_list.pop_right())
# print("list tail:", my_list.tail.value)
# print("list length:", my_list._length)


# print(empty_list.pop_left())
# print(empty_list.pop_right())

# print(one_element_list.head.value)
# print(one_element_list.tail.value)
# print(one_element_list.pop_left())
# print(one_element_list.head)
# print(one_element_list.tail)
# print(one_element_list._length)

# print(one_element_list.head.value)
# print(one_element_list.tail.value)
# print(one_element_list.pop_right())
# print(one_element_list.head)
# print(one_element_list.tail)
# print(one_element_list._length)

# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.prepend(2)

# my_list.remove(3)
# my_list.remove(7)


# print("head value:", my_list.head.value)
# print("tail value:", my_list.tail.value)

# alphabetical_list = SinglyLinkedList()

# alphabetical_list.append(1)
# alphabetical_list.append(2)
# alphabetical_list.append(3)
# alphabetical_list.append(4)
# alphabetical_list.append(5)
# alphabetical_list.append(6)

# print(alphabetical_list.head.value)
# print(alphabetical_list.tail.value,"\n")

# alphabetical_list.reverse()

# print(alphabetical_list.head.value)
# print(alphabetical_list.head.next.value)
# print(alphabetical_list.head.next.next.value)
# print(alphabetical_list.head.next.next.next.value)
# print(alphabetical_list.head.next.next.next.next.value)
# print(alphabetical_list.tail.value)
# print(alphabetical_list.tail.next)

# alphabetical_list = SinglyLinkedList()

# alphabetical_list.append(1)
# alphabetical_list.append(2)
# alphabetical_list.append(3)
# alphabetical_list.append(4)
# alphabetical_list.append(5)
# alphabetical_list.append(6)

# print(alphabetical_list.valuelist())

# alphabetical_list.reverse()

# print(alphabetical_list.valuelist())