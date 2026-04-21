"""a queue"""

from modules.nodes import Node_singly_linked as Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def peek(self):
        """returns the value of the top item in the stack without removing it"""
        if self.front == None:
            return "Empty"
        return self.front.data

    def enqueue(self, data):
        """adds a node to the end of the queue"""
        temp = Node(data)
        if self.rear == None: #if the queue is totally empty
            self.rear = self.front = temp #i didnt know you could do assigment like this
            return #instead of an else

        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        """removes a node from the front of the queue"""
        if self.front == None:
            return "Empty, cannot dequeue item."
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp.data
        
    def __len__(self): #added 4/16
        if self.front == None or self.rear == None:
            return 0
        current_node = self.front
        length = 1

        while(current_node.next != None):
            length += 1
            current_node = current_node.next

        return length


    def __str__(self):
        if self.rear == None or self.front == None:
            return "Empty"
        
        current_node = self.front
        output_string = ""

        while(current_node.next != None):
            output_string += str(current_node.data) + ", "
            current_node = current_node.next
        output_string = "[" + output_string + str(current_node.data) +"]"
        return output_string