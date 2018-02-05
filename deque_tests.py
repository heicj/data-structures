import unittest
from deque import Node, Deque

class TestIt(unittest.TestCase):
	
	def test_1(self):
		"""test creating a node"""
		n1 = Node('A')
		self.assertEqual(n1._value, "A")
		
	def test_2(self):
		"""test append to empty deque"""
		n1 = Node('A')
		d = Deque()
		d.append(n1)
		self.assertEqual(d.front._value, "A")
		self.assertEqual(d.rear._value, "A")
		size = len(d)
		self.assertEqual(size, 1)
		
	def test_3(self):
		"""test append to list with node"""
		pass