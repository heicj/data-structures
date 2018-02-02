import unittest
from stack import Node, Stack

class TestIt(unittest.TestCase):
	def test_1(self):
		"""test creating a node"""
		n1 = Node('A')
		self.assertEqual(n1._value, 'A')
		
	def test_2(self):
		"""test push to top of stack"""
		n1 =Node('A')
		s = Stack()
		s.push(n1)
		self.assertEqual(s.top._value, 'A')
	
	def test_3(self):
		"""test that second item pushed to stack is top"""
		n1 = Node('A')
		n2 = Node('B')
		s = Stack()
		s.push(n1)
		s.push(n2)
		self.assertEqual(s.top._value, 'B')
		
	def test_4(self):
		"""test that pop returns top of stack"""
		n1 = Node('A')
		n2 = Node('B')
		s = Stack()
		s.push(n1)
		s.push(n2)
		returned = s.pop()
		self.assertEqual(returned._value, 'B')
		
	def test_5(self):
		"""test that top of stack changes after pop"""
		n1 = Node('A')
		n2 = Node('B')
		s = Stack()
		s.push(n1)
		s.push(n2)
		s.pop()
		self.assertEqual(s.top._value, 'A')
		
	def test_6(self):
		"""test that using pop on one node stack works"""
		n1 = Node('A')
		s = Stack()
		s.push(n1)
		s.pop()
		self.assertEqual(s.top, None)
	
	def test_7(self):
		s = Stack()
		s.pop()
		self.assertEqual(None, None)
		
	
		
		