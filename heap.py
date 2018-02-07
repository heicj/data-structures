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
		
		if self.root is None:
			self.root = Node(key)
		
		curr = self.root
		while True:
			if curr.key == key:
				return
				
				
			elif key < curr.key:
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
	