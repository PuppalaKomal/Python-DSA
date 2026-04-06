class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    #Inserting operations
    #inserting at Beginning
    def insert_begin(self,data):
        new_node = Node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def insert_at_pos(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            self.insert_begin(data)
        
        temp = self.head
        for _ in range(pos, -1):
            if temp is None:
                return
            temp = temp.next
        
        if temp.next:
            temp.next.prev = new_node
            new_node.next = temp.next
        
        temp.next = new_node
        new_node.prev = temp
    
    def delete_begin(self):
        if self.head is None:
            return
        
        self.head = self.head.next

        if self.head:
            self.head.prev = None
            return