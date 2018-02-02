import unittest
from linked_list import Node, LinkedList

class TestIt(unittest.TestCase):
	def test_1(self):
		"""test creating a node"""
		n1 = Node('A')
		self.assertEqual(n1._value, 'A')
		
	def test_2(self):
		"""test append method"""
		n1 = Node('A')
		link = LinkedList()
		link.append(n1)
		self.assertEqual(link._head._value, 'A')
		
	def test_3(self):
		"""test pop returns correct node"""
		n1 = Node('A')
		n2 = Node('B')
		link = LinkedList()
		link.append(n1)
		link.append(n2)
		node = link.pop()
		self.assertEqual(node._value, 'A')
	
	def test_4(self):
		"""test that pop off only item in list that head becomes None"""
		n1 = Node('A')
		link = LinkedList()
		link.append(n1)
		link.pop()
		self.assertEqual(link._head, None)
		
	def test_5(self):
		"""test pop on empty list"""
		link = LinkedList()
		link.pop()
		self.assertEqual(None, None)
		
	"""def test_6(self):
		test remove
		n1 = Node('A')
		n2 = Node('B')
		n3 = Node('C')
		link = LinkedList()
		link.append(n1)
		link.append(n2)
		link.append(n3)
		link.remove(n2)
		self.assertEqual(head._next._value, 'C')
	"""
	
	def test_7(self):
		n1 = Node('A')
		n2 = Node('B')
		n3 = Node('C')
		link = LinkedList()
		link.append(n1)
		link.append(n2)
		link.append(n3)
		dis = link.display()
		self.assertEqual(['A','B','C'], ['A','B','C'])
		