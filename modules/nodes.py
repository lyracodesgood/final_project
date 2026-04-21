"""this file describes the node class, it has been altered for the binary
tree structure"""

class Node_binary_tree():
    def __init__(self, data):
        self.data = data #some data
        self.left = None #link to the left
        self.right = None #link to the right

    def __str__(self):
        return str(self.data)
    
class Node_singly_linked():
    def __init__(self, data):
        self.data = data #some data
        self.next = None

    def __str__(self):
        return str(self.data)