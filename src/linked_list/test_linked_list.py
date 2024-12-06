import unittest
from linked_list import Linked_list

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = Linked_list()
    
    def test_insert_begin(self):
        self.linked_list.insert_begin(10)
        self.linked_list.insert_begin(20)
        self.assertEqual(self.linked_list.head.data, 20)
        self.assertEqual(self.linked_list.head.next.data, 10)
    
    def test_insert_end(self):
        self.linked_list.insert_end(30)
        self.linked_list.insert_end(40)
        current = self.linked_list.head
        while current.next:
            current = current.next
        self.assertEqual(current.data, 40)

    def test_insert_instead_of(self):
        self.linked_list.insert_begin(10)
        self.linked_list.insert_begin(20)
        self.linked_list.insert_instead_of(15, 10)
        current = self.linked_list.head
        while current and current.data != 15:
            current = current.next
        self.assertIsNotNone(current)
        self.assertEqual(current.data, 15)

    def test_remove_begin(self):
        self.linked_list.insert_begin(10)
        self.linked_list.insert_begin(20)
        self.linked_list.remove_begin()
        self.assertEqual(self.linked_list.head.data, 10)
    
    def test_remove_end(self):
        self.linked_list.insert_end(30)
        self.linked_list.insert_end(40)
        self.linked_list.remove_end()
        current = self.linked_list.head
        while current.next:
            current = current.next
        self.assertEqual(current.data, 30)

    def test_remove_node(self):
        self.linked_list.insert_end(50)
        self.linked_list.insert_end(60)
        self.linked_list.insert_end(70)
        self.linked_list.remove_node(60)
        current = self.linked_list.head
        while current:
            self.assertNotEqual(current.data, 60)
            current = current.next
unittest.main()