class Node(object):
	_next = None
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
			self.rear = node
		
		self.size += 1
		
	def appendleft(self, node):
		"""adds a value to the front of the deque"""
		if self.front is None:
			self.front = node
			self.rear = node
		else:
			node._next = self.front
			self.front = node
		
		self.size += 1
	
	def pop(self): 
		""" removes a value from the end of the deque and returns it raises exception if empty """
		if self.front is None:
			raise exception('Empty deque')
		else:
			curr = self.front
			pop = curr
			while curr._next is not None:
				pop = curr
				curr = curr._next
				if curr._next == None:
					self.rear = curr
					return pop
			
			self.size -= 1
	
	def popleft(self):
		""" removes a value from the front of the deque and returns it raises exception if empty"""
		if self.front is None:
			raise ValueError
		else:
			curr = self.front
			self.front = self.front._next
			self.size -= 1
			return curr
			
	
	def peek(self):
		"""
		returns the next value that would be returned by pop but leaves the value
		in the deque. Returns None if empty
		"""
		if self.front is None:
			return None
		else:
			val = self.rear
			return val
		
	
	def peekleft(self):
		"""
		returns the next value that would be returned by popleft but leaves the value in the deque
		returns None if deque is empty
		"""
		if self.front is None:
			return None
		else:
			val = self.front
			return val
		
	def __len__(self):
		""" returns the count of the items in the deque returns 0 if empty """
		if self.size == 0:
			return 0
		else:
			return self.size