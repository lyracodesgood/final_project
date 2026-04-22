"""in this file i implement a linked list"""
from modules.nodes import Node_singly_linked as Node

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data): 
        """appends a value to the end of the linked list"""
        if(self.head == None): #if empty
            self.head = Node(data)
            return
        current_node = self.head
        while(current_node.next != None): #while there is a link
            current_node = current_node.next
        current_node.next = Node(data)

    def prepend(self, data):
        """prepends a value to the start of the linked list"""
        if(self.head == None): #if empty
            self.head = Node(data)
            return 
        prior_node = self.head #store previous node
        self.head = Node(data) #new first node
        self.head.next = prior_node #previous node is now linked by the new 1st

        # new_node = Node(data)
        # new_node.next = self.head
        # self.head = new_node      
        # #slightly better implementation above, can drop the if statement at
        #the start


    def __len__(self):
        """returns the length of the linked list"""
        if(self.head == None):
            return 0
        
        count = 1
        current_node = self.head
        while(current_node.next != None):
            count += 1
            current_node = current_node.next
        return count

    def __str__(self):
        """prints all values in the linked list nicely"""
        if(self.head == None):
            return "Empty" #early return to avoid nesting
        
        return_string = ""
        current_node = self.head
        while(current_node.next != None): #while there is a link
            return_string = return_string + "'" + str(current_node.data) + "', "
            current_node = current_node.next #follow link to next item
        # still need to add the last linked node's data after all that
        return_string = "[" + return_string + str(current_node.data) + "]"
        return return_string

    def __iter__(self):
        """i hope it work :)"""
        self.active_node = self.head
        return self
    

    def __next__(self):
        """i really hope"""
        if self.active_node == None:
            raise StopIteration
        return_node = self.active_node
        self.active_node = self.active_node.next
        return return_node #it works
    
    def __add__(self, other):
        """making it so i can add them together for fun"""
        return_linked_list = LinkedList()
        return_linked_list.append(self.head)
        for node in self:
            return_linked_list.append(node)
        return_linked_list.append(other.head)
        for node in other:
            return_linked_list.append(node)
        return return_linked_list
    
    def __contains__(self, target_data):
        """returns true if the target is in the list"""
        current_node = self.head
        while(current_node != None):
            if current_node.data == target_data:
                return True
            current_node = current_node.next
        return False

    def __getitem__(self, index):
        count = 0
        current_node  = self.head
        if(index == 0):
            return current_node
        while(current_node.next != None):
            current_node = current_node.next
            count += 1
            if(index == count): 
                return current_node
                break
        return current_node #in case we get to the end first
    
    def __setitem__(self, index, data):
        if(index == 0):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        prior_node: Node #changed this, if it breaks look at other version
        while(current_node.next != None and index >= 1): #changed this to >= from >
            index -= 1
            prior_node = current_node
            current_node = current_node.next
            
        new_node = Node(data)
        prior_node.next = new_node
        new_node.next = current_node.next
    
    def insert(self, index, data):
        if(index == 0):
            self.prepend(data)
            return
        
        # prior_node : Node
        current_node = self.head
        while(current_node.next != None and index > 1): #get us there
            index -= 1
            current_node = current_node.next #move forward

        # insertable_node = Node(data) #the new guy
        # prior_node.next = insertable_node 
        # insertable_node.next = current_node #old terrible method

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
        #THIS IS HOW TO DO IT

    def pop(self, index):
        """removes the item at the specified index and returns it"""
        current_node = self.head
        if index == 0:
            self.head = self.head.next
            return current_node
        
        #traverse
        while(current_node.next != None and index > 1):
            index -= 1
            current_node = current_node.next
        
        #switch around and give em back
        return_node = current_node.next
        current_node.next = current_node.next.next
        return return_node

    def remove(self, data):
        """removes the first occurence of an item"""
        current_node = self.head
        while(current_node.next != None):
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
