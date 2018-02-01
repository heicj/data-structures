class Node(object):
	_value = 0
	_next = None
	
	def __init__(self, value):
		self._value = value
	
	def next(self, next):
		self._next = next	
		
	def value(self):
		return self._value
		
class LinkedList(object):
	_head = None
	_tail = None
	_length = 0
	
	def __init__(self):
		pass
	
	def append(self, node):
		
		if self._head is None:
			self._head = self._tail = node
		else:
			curr = self._head	
			#find the end of the list(tail)
			while curr:
				if curr._next is None:
					curr._next = node
					break
		self._length += 1
		
			
	def pop(self):
		if self.head is None:
			return None
		#non - empty list - get (return) the node at the head, and 
		#reset the head to the next head in the list
		else:
			node = self.head
			self.head = self.head._next
			self.size -= 1
			return node
		
	def size(self):
		return self._length
		
	def search(self, val):
		if self._head is None:
			return None
		else:
			curr = self._head
			while curr._value is not val:
				curr = curr._next
			
			
			return curr 
		
	def remove(self, node):
		prev = None
		curr = self.head
		while curr is not None:
			if curr._value == value:
				if prev is not None:
					prev._next = curr._next
					if curr._next is not None:
						curr._next._prev = prev
				
				if self.head == curr:
					self.head = curr._next
				if self.tail == curr:
					self.tail = curr._prev
				break
			else:
				prev = curr
				curr = curr._next
		
	def display(self):
		curr = self._head