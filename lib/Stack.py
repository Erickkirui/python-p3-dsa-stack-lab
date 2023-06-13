
import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for index in range(len(expected)):
            self.assertEqual(expected[index], stk.items[index])

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1,2,3,4,5])
        stk.push(0)
        expected = [1,2,3,4,5,0]
        for index in range(len(expected)):
            self.assertEqual(expected[index], stk.items[index])

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1,2,3,4,5])
        stk.pop()
        expected = [1,2,3,4]
        for index in range(len(expected)):
            self.assertEqual(expected[index], stk.items[index])

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        self.assertEqual(stk.size(), len(expected))

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        self.assertTrue(stk.isEmpty())
        self.assertEqual(stk.size(), 0)
        self.assertIsNone(stk.pop())
        stk.push(1)
        self.assertFalse(stk.isEmpty())
        self.assertEqual(stk.size(), 1)
        self.assertEqual(stk.pop(), 1)

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)

        self.assertTrue(stk.full())
        self.assertEqual(stk.size(), 1)
        self.assertEqual(stk.pop(), 1)
        stk.push(1)
        stk.push(2)
        self.assertTrue(stk.full())
        self.assertEqual(stk.size(), 1)
        self.assertEqual(stk.pop(), 1)

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack
