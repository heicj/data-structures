class Node(object):
	_value = 0
	_next = None
	_prev = None
	
	def __init__(self, value):
		self._value = value
	
	def next(self, next):
		self._next = next	
		
	def value(self):
		return self._value
		
class LinkedList(object):
	_head = None
	_tail = None
	_size = 0
	
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
		self._size += 1
		
			
	def pop(self):
		if self._head is None:
			return None
		#non - empty list - get (return) the node at the head, and 
		#reset the head to the next head in the list
		else:
			node = self._head
			self._head = self._head._next
			self._size -= 1
			return node
		
	def size(self):
		return self._size
		
	def search(self, val):
		if self._head is None:
			return None
		else:
			curr = self._head
			while curr._value is not val:
				curr = curr._next
			
			
			return curr 
		
	def remove(self, value):
		prev = None
		curr = self._head
		while curr is not None:
			if curr._value == value:
				if prev is not None:
					prev._next = curr._next
					if curr._next is not None:
						curr._next._prev = prev._next
				
				elif self._head == curr:
					self._head = curr._next
				elif self._tail == curr:
					self._tail = curr._prev
				break
			else:
				prev = curr
				curr = curr._next
		
	
	def display(self):
		curr = self._head
		items = []
		while curr._next is not None:
			items.append(curr._value)
		return items
			
		
	def __len__(self):
		return(self._size)