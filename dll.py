class Node(object):
	_value = 0
	_next = None
	_prev = None
	
	def __init__(self, value):
		self._value = value
		
class DoubleLinkedList(object):
	head = None
	tail = None
	current = None
	size = 0
	
	def __init__(self):
		pass
		
	def push(self, node):
		curr = self.head
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			curr._next = node
			node._prev = curr
			self.tail = node._prev
			self.head = node
		self.size += 1
			
	def append(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail._next = node
			node._prev = self.tail
			self.tail = node
			self.size += 1
	
	def pop(self):
		if self.head is None:
			return None
		
		elif self.head is self.tail:
			return head
		else:
			node = self.head
			self.head = self.head._next
			self.size -= 1
			return node
	
	
	def shift(self):
		currT = self.tail
		if self.tail is None:
			raise Exception("empty list")
		elif self.head is self.tail:
			return tail
		else:
			node = self.tail
			self.tail = self.tail._prev
			self.size -= 1
		return self.tail
	
		
	def forward(self):
		if self.current is None:
			self.current = self.head
			
		else:
			self.current = self.current._next
		return self.current
		
	def backward(self):
		if self.current is None:
			self.current = self.tail
		else:
			self.current = self.current._prev
		return self.current
	
	def remove(self, value):
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
				self.size += 1
				break
			else:
				prev = curr
				curr = curr._next
				

