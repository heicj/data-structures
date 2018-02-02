import unittest
from queue import Node, Queue

class TestIt(unittest.TestCase):
	
	def test_1(self):
		"""test creating a node"""
		n1 = Node('A')
		self.assertEqual(n1._value, 'A')
		
	def test_2(self):
		"""test enqueue"""
		n1 = Node('A')
		q = Queue()
		q.enqueue(n1)
		self.assertEqual(q.front._value, 'A')
		
	def test_3(self):
		"""test enqueue"""
		n1 = Node('A')
		n2 = Node('B')
		q = Queue()
		q.enqueue(n1) #A goes in queue first
		q.enqueue(n2) #B goes in queue second, so end of the queue
		self.assertEqual(q.front._next._value, 'B')  #test that the head, A's next property is B
		
	def test_4(self):
		"""test dequeue"""
		n1 = Node('A')
		n2 = Node('B')
		q = Queue()
		q.enqueue(n1) #A goes into queue first
		q.enqueue(n2) #B goes second
		q.dequeue() #dequeue removes A
		self.assertEqual(q.front._value, 'B') #tests that B is fron of the queue
		
	def test_5(self):
		"""test to check len method works"""
		n1 = Node('A')
		n2 = Node('B')
		q = Queue()
		q.enqueue(n1) 
		q.enqueue(n2)
		self.assertEqual(len(q), 2)
		
		