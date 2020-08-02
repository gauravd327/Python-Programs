class Node():
    def __init__(self, value):
        self.value = value
        self.pointer = None
        
        
class Linked_List():
    def __init__(self):
        self.head = None
        self.counter = 0

    def print_list(self):
        temp = self.head
        while temp:
            if temp.pointer == None:
                print(temp.value)
                break
            print(end=str(temp.value) + " -> " ),
            temp = temp.pointer

    def add_node(self, value):
        currentNode = Node(value)
        self.counter = 1
        if self.head == None:
            self.head = currentNode
        else:
            temp = self.head
            while temp:
                self.counter += 1
                if temp.pointer == None:
                    temp.pointer = currentNode
                    break
                temp = temp.pointer

    def remove_node(self, value):
        temp = self.head
        if temp.pointer == None:#Doesn't fully remove the node if the length of the linked list is 1
            temp.value = None
        else:
            while temp.pointer.value != value:
                if temp.pointer == None:
                    break
                
                temp = temp.pointer
            temp.pointer = None
            self.counter -= 1

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





