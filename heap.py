class Node(object):
	
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		
class Heap(object):
	"""min heap; sorted with smallest values at top"""
	
	def __init__(self):
		self.root = None
		
	def push(self, key):
		"""inserts into proper place in heap"""
		if self.root is None:
			self.root = Node(key)

		curr = self.root
		while True:
			if curr.key == key:
				return
				
				
			elif self.key < curr.key:
				if curr.left is None:
					curr.left = Node(key)
				else:
					curr = curr.left
					
			else:
				if curr.right is None:
					curr.right = Node(key)
					return
				else:
					curr = curr.right
	
	def pop(self):
		"""removes top of heap"""
		if self.root is None:
			return None
			
		if self.root is not None:
			curr = self.root
			
			if curr.left is None:
				if curr.right is None:
					self.root = None
					return curr
			
			
			
			