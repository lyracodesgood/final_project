"""da stack"""

from modules.nodes import Node_singly_linked as Node

class Stack():
    def __init__(self):
        self.top = None
    
    def push(self, data):
        """pushes an item onto the top of the stack"""
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        """removes the item at the top of the stack and returns it"""
        if self.top == None:
            return "Empty"
        
        temp = self.top
        self.top = self.top.next
        return temp.data #this had to be changed to temp.data because it was giving me the wrong nodes in my tree leading to errors
        
    def peek(self):
        """returns the value of the top item in the stack without removing it"""
        if self.top == None:
            return "Empty"
        return self.top.data

    def __str__(self):
        if self.top == None:
            return "Empty"
        
        current_node = self.top

        output_string = ""
        while(current_node.next != None):

            output_string += str(current_node.data) + ", "
            current_node = current_node.next

        output_string ="[" + output_string + str(current_node.data) + "]"

        return output_string
