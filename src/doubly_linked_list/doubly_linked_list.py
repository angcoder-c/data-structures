class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

    def __repr__(self):
        back_data = self.back.data if self.back else None
        next_data = self.next.data if self.next else None
        return f'[{back_data}|{self.data}|{next_data}]'


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)

    def insert_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.back = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.back = current

        
    def insert_instead_of(self, data, other_data):
        if not self.head: return

        new_node = Node(data)
        current = self.head

        if current.data == other_data:
            new_node.next = self.head.next
            self.head.back = new_node.back
            self.head = new_node
            return

        while current and current.data != other_data:
            current = current.next

        if not current:  return


        new_node.next = current.next
        new_node.back = current.back
        
        if current.back:
            current.back.next = new_node

        current.back = new_node

    def remove_begin(self): 
        if not self.head: return
        if not self.head.next:
            self.head=None
            return
        self.head=self.head.next
        self.head.back=None

    def remove_end(self):
        if not self.head: return
        if not self.head.next:
            self.head=None
            return
        current=self.head
        while current.next.next:
            current=current.next
        current.next=None

    def remove_node(self, data):
        if not self.head: return

        if self.head.data == data:
            if not self.head.next:
                self.head = None
            else:
                self.head = self.head.next
                self.head.back = None
            return

        current = self.head
        while current and current.data != data:
            current = current.next

        if not current: return

        if not current.next:
            current.back.next = None
            return

        current.back.next = current.next
        current.next.back = current.back


