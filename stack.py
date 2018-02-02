class Node(object):
	_value = 0
	_next = None
	
	def __init__(self, value):
		self._value = value
		
class Stack(object):
	size = 0
	top = None
	
	def __init__(self):
		pass
	
	def push(self, node):
		node.next = self.top
		self.top = node
		self.size += 1
	
	def pop(self):
		if self.top is None:
			return None
			
		node = self.top
		self.top = node.next
		self.size -= 1
		
		return node
		
	def __len__(self):
		return self.size	