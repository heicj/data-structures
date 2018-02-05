class Node(object):
	_next = None
	_prev =None
	_value = 0
	
	def __init__(self, value):
		self._value = value
		
class Deque(object):
	front = None
	rear = None
	size = 0
	
	def __init__(self):
		pass
		
	def append(self, node):
		"""adds value to end of the deque"""
		if self.front is None:
			self.front = node
			self.rear = node
		else:
			self.rear._next = node
			node._prev = self.rear
			self.rear = node
		
		self.size += 1
		
	def appendleft(node):
		"""adds a value to the front of the deque"""
	
	def pop():
		"""
		removes a value from the end of the deque and returns it
		raises exception if empty
		"""
	
	def popleft():
		"""
		removes a value from the front of the deque and returns it
		raises exception if empty
		"""
		
	def peek():
		"""
		returns the next value that would be returned by pop but leaves the value
		in the deque. Returns None if empty
		"""
	
	def peekleft():
		"""
		returns the next value that would be returned by popleft but leaves the value in the deque
		returns None if deque is empty
		"""
		
	def __len__(self):
		"""
		returns the count of the items in the deque
		returns 0 if empty
		"""
		if self.size == 0:
			return 0
		else:
			return self.size