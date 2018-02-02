class Node(object):
	_value = 0
	_next = None
	
	def __init__(self, value):
		self._value = value
	
class Queue(object):
	front = None
	size = 0
	
	def __init__(self):
		pass
	
	def enqueue(self, node):
		"""add to the back of the queue"""
		if self.front is None:
			self.front = node
		else:
			curr = self.front	
			while curr._next is not None:
				curr = curr._next
			curr._next = node
		self.size += 1
	
	def dequeue(self):
		"""remove from front of the queue"""
		if self.front is None:
			return None
		else:
			node = self.front
			self.front = node._next
			self.size -= 1
		
	def __len__(self):
		return self.size