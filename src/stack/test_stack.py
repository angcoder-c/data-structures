import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(self.stack.push(0), 0)
        self.assertEqual(self.stack.push(1), 1)
        self.assertEqual(self.stack.push(2), 2)
        self.assertEqual(self.stack.push(3), 3)
        self.assertEqual(self.stack.stack, [0, 1, 2, 3])

    def test_pop(self):
        for i in range(4):
            self.stack.push(i)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.stack, [0, 1])
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)
        self.assertEqual(self.stack.stack, []) 

    def test_combined_operations(self):
        for i in range(2):
            for j in range(4):
                if i == 0:
                    self.stack.push(j)
                else:
                    if j != 0 and j != 3:
                        self.stack.pop()
                    if j == 3:
                        self.assertEqual(self.stack.pop(), 0)  # FILO
                    if j == 0:
                        self.assertEqual(self.stack.pop(), 3)  # LIFO

unittest.main()
