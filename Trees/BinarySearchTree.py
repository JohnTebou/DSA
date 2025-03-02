class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		new_node = Node(value)
		if not self.root:
			self.root = new_node
		curr = self.root
		while value != curr.value:
			if value < curr.value:
				if not curr.left:
					curr.left = new_node
					break
				curr = curr.left
			else:
				if not curr.right:
					curr.right = new_node
					break
				curr = curr.right
		return self
	
	def contains(self, value):
		curr = self.root
		while curr:
			if curr.value == value:
				return True
			elif value > curr.value:
				curr = curr.right
			else:
				curr = curr.left
		return False
	
	def remove(self, value):