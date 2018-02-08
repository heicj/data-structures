import unittest
import pytest
from heap import Node, Heap

class TestIt(unittest.TestCase):

	def test_1(self):
		"""empty tree"""
		h = Heap()
		h.push(2)
		self.assertEqual(h.root.key, 2)
			
	def test_2(self):
		"""insert left"""
		n1 = Node(2)
		n2 = Node(3)
		h = Heap()
		h.push(n1)
		h.push(n2)
		self.assertEqual(h.root.left.key, 3)
			
	def test_3(self):
		"""insert right"""
		h = Heap()
		h.push(5)
		h.push(2)
		h.push(8)
		self.assertEqual(h.root.right.key, 8)
		
	def test_4(self):
		"""pop from empty heap"""
		h = Heap()
		self.assertEqual(h.pop(), None)
		
	def test_5(self):
		"""pop with only one item in heap"""
		h = Heap()
		h.push(3)
		v = h.pop()
		self.assertEqual(v.key, 3)
		
	def test_6(self):
		pass