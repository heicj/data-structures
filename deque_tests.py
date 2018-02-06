import unittest
import pytest
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
		"""test append to deque that has a node"""
		n1 = Node('A')
		n2 = Node('B')
		d = Deque()
		d.append(n1)
		d.append(n2)
		self.assertEqual(d.rear._value, "B")
		self.assertEqual(d.front._value, "A")
		size = len(d)
		self.assertEqual(size, 2)
		
	def test_4(self):
		"""test adding to front of empty deque"""
		n1 = Node('A')
		d = Deque()
		d.appendleft(n1)
		self.assertEqual(d.rear._value, "A")
		self.assertEqual(d.front._value, "A")
		self.assertEqual(len(d), 1)
		
	def test_5(self):
		"""test append left"""
		n1 = Node('A')
		n2 = Node('B')
		d = Deque()
		d.appendleft(n1)
		d.appendleft(n2)
		self.assertEqual(d.front._value, 'B')
		self.assertEqual(d.rear._value, 'A')
		self.assertEqual(len(d), 2)
		
	
	"""def test_6(self):
		n1 = Node('A')
		n2 = Node('B')
		n3 = Node('C')
		d = Deque()
		d.appendleft(n1)
		d.appendleft(n2)
		d.appendleft(n3)
		res = d.pop()
		self.assertEqual(res._value, "B")
	"""
	
	def test_7(self):
		"""test that error is raised when popleft is used on empty deque"""
		d = Deque()
		with self.assertRaises(ValueError):
			d.popleft()
	
	def test_8(self):
		"""test popleft when nodes exist in it"""
		n1 = Node('A')
		n2 = Node('B')
		d = Deque()
		d.append(n1)
		d.append(n2)
		res = d.popleft()
		self.assertEqual(res._value, "A")
		self.assertEqual(d.front._value, "B")
		