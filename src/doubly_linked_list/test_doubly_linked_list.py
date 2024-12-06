import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_insert_begin(self):
        self.dll.insert_begin(10)
        self.assertEqual(str(self.dll), "10")
        self.dll.insert_begin(20)
        self.assertEqual(str(self.dll), "20 <-> 10")
        self.dll.insert_begin(30)
        self.assertEqual(str(self.dll), "30 <-> 20 <-> 10")

    def test_insert_end(self):
        self.dll.insert_end(10)
        self.assertEqual(str(self.dll), "10")
        self.dll.insert_end(20)
        self.assertEqual(str(self.dll), "10 <-> 20")
        self.dll.insert_end(30)
        self.assertEqual(str(self.dll), "10 <-> 20 <-> 30")

    def test_insert_instead_of(self):
        self.dll.insert_end(10)
        self.dll.insert_end(20)
        self.dll.insert_end(30)
        self.dll.insert_instead_of(15, 20)
        self.assertEqual(str(self.dll), "10 <-> 15 <-> 30")
        self.dll.insert_instead_of(5, 10)
        self.assertEqual(str(self.dll), "5 <-> 15 <-> 30")

    def test_remove_begin(self):
        self.dll.insert_end(10)
        self.dll.insert_end(20)
        self.dll.insert_end(30)
        self.dll.remove_begin()
        self.assertEqual(str(self.dll), "20 <-> 30")
        self.dll.remove_begin()
        self.assertEqual(str(self.dll), "30")
        self.dll.remove_begin()
        self.assertEqual(str(self.dll), "")

    def test_remove_end(self):
        self.dll.insert_end(10)
        self.dll.insert_end(20)
        self.dll.insert_end(30)
        self.dll.remove_end()
        self.assertEqual(str(self.dll), "10 <-> 20")
        self.dll.remove_end()
        self.assertEqual(str(self.dll), "10")
        self.dll.remove_end()
        self.assertEqual(str(self.dll), "")

    def test_remove_node(self):
        self.dll.insert_end(10)
        self.dll.insert_end(20)
        self.dll.insert_end(30)
        self.dll.remove_node(20)
        self.assertEqual(str(self.dll), "10 <-> 30")
        self.dll.remove_node(10) 
        self.assertEqual(str(self.dll), "30")
        self.dll.remove_node(30)
        self.assertEqual(str(self.dll), "")
        self.dll.remove_node(40)  
        self.assertEqual(str(self.dll), "")

unittest.main()
