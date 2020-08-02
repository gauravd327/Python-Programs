class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None
        
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.counter = 0
        
    
    def print_list(self):
        temp = self.head
        while temp:
            if temp.pointer == None:
                print(temp.value)
                break
            print(end=str(temp.value) + " -> "),
            temp = temp.pointer
            
    
    def add_node(self, value):
        currentNode = Node(value)
        if self.head == None:
            self.counter = 1
            self.head = currentNode
        else:
            self.counter += 1
            currentNode.pointer = self.head
            self.head = currentNode
            

    def remove_node(self, value):
        if self.head.value != value:
            print("Number is not at the beginning of the list")
        else:
            self.counter -= 1
            nextNode = self.head.pointer
            self.head = nextNode
            
            
    def list_length(self):
        print("The length of the list is: " + str(self.counter))
            

        

llist = Linked_List()


llist.add_node(10)
llist.list_length()
llist.print_list()

llist.add_node(8)
llist.list_length()
llist.print_list()

llist.add_node(12)
llist.list_length()
llist.print_list()

llist.add_node(7)
llist.list_length()
llist.print_list()

llist.remove_node(7)
llist.list_length()
llist.print_list()


              