import unittest
from dll import Node, DoubleLinkedList

class TestIt(unittest.TestCase):
	
	def test_1(self):
		"""make a node"""
		n1 = Node('A')
		self.assertEqual(n1._value, 'A')
	
	def test_2(self):
		"""make a test head is set when add first node"""
		n1 = Node('A')
		dl = DoubleLinkedList()
		dl.append(n1)
		self.assertEqual(dl.head._value, 'A')
		
	def test_3(self):
		"""add two nodes. test that 2nd append makes changes tail to new node"""
		n1 = Node('A')
		n2 = Node('B')
		dl = DoubleLinkedList()
		dl.append(n1)
		dl.append(n2)
		self.assertEqual(dl.tail._value, 'B')
		
	def test_4(self):
		"""check that head is still the first node added to list"""
		n1 = Node('A')
		n2 = Node('B')
		dl = DoubleLinkedList()
		dl.append(n1)
		dl.append(n2)
		self.assertEqual(dl.head._value, 'A')
		
	def test_5(self):
		"""check that push adds to front"""
		n1 = Node('A')
		n2 = Node('B')
		dl = DoubleLinkedList()
		dl.append(n1)
		dl.append(n2)
		n3 = Node('C')  #will push C to front(head)
		dl.push(n3)
		self.assertEqual(dl.head._value, 'C')
		
	def test_6(self):
		"""check that pop removes head"""
		n1 = Node('A')
		n2 = Node('B')
		dl = DoubleLinkedList()
		dl.append(n1) #head and tail at this point
		dl.append(n2) # A is head and B is now tail
		dl.pop() # removes A so head value should be B
		self.assertEqual(dl.head._value, 'B') 
		
	def test_7(self):
		"""check that shift removes last node"""
		n1 = Node('A')
		n2 = Node('B')
		n3 = Node('C')
		dl = DoubleLinkedList()
		dl.append(n1)
		dl.append(n2)
		dl.append(n3)
		dl.shift()
		self.assertEqual(dl.tail._value, 'B')
	
	def test_8(self):
		"""test to remove tail by using remove method"""
		n1 = Node('A')
		n2 = Node('B')
		n3 = Node('C')
		dl = DoubleLinkedList()
		dl.append(n1)
		dl.append(n2)
		dl.append(n3)
		dl.remove('C')  #this removes C so tail should become BaseException
		self.assertEqual(dl.tail._value, 'B')
		
		
		
		
		
	
		