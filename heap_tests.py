import unittest
import pytest
from heap import Node, Heap

class TestIt(unittest.TestCase):

	def test_1(self):
		"""empty tree"""
		h = Heap()
		h.push(1)
		self.assertEqual(h.root.key, 1)
			
	def test_2(self):
		"""insert left"""
		h = Heap()
		h.push(5)
		h.push(4)
		self.assertEqual(h.root.left.key, 4)
			
	def test_3(self):
		"""insert right"""
		h = Heap()
		h.push(5)
		h.push(2)
		h.push(8)
		self.assertEqual(h.root.right.key, 8)