class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self):
        self.head = None
    def insert_beginn(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def traverse(self):
        current = self.head
        while current:
            #print(current)
            print(current.data,end =" -> ")
            current = current.next
        
        print("None")
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next :
            current = current.next
        current.next = new_node
    def deletion_at_end(self):
        if self.head == None:
            print("linklist is empty")
            return
        if self.head.next == None :
            self.head = None
            return
        current = self.head
        while current.next.next :
            current = current.next
        current.next = None
    def deletion_at_beggin(self):
        if self.head == None:
            print("linklist is empty")
            return
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next 
    def search_in_ll(self,target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            current = current.next
        return False
if __name__ == "__main__" :
    l1 = linklist()
    l1.insert_beginn(3)
    l1.insert_beginn(21)
    l1.insert_beginn(4)
    l1.insert_beginn(8)
 #   l1.traverse()
    l1.insert_at_end(12)
  #  l1.traverse()
    l1.deletion_at_end()
  #  l1.traverse()
    l1.deletion_at_beggin()
    l1.traverse()
   