class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        back_data = self.back.data if self.back else None
        next_data = self.next.data if self.next else None
        return f'[{back_data}|{self.data}|{next_data}]'

class Linked_list:
    def __init__(self):
        self.head = None
    
    def __repr__ (self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

    def insert_begin(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_instead_of(self, data, other_data):
        if not self.head:  return
        current = self.head
        while current and current.data != other_data:
            current = current.next
        if current: 
            new_node = Node(data=data)
            new_node.next = current.next
            current.next = new_node

    def remove_begin(self):
        if not self.head: return
        self.head = self.head.next

    def remove_end(self):
        if not self.head: return
        if not self.head.next: 
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_node(self, data):
        if not self.head: return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data: 
            current = current.next
        if current.next: 
            current.next = current.next.next