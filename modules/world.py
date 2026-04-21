"""a file containing classes for the dungeon crawler, like player and room"""
from modules.stack import Stack
from modules.linked_list import LinkedList

class Room():
    def __init__(self, id, title, description, events):
        """creates a room object, events must be iterable"""
        self.id = id
        self.title = title
        self.description = description
        self.events = Stack()
        for item in events:
            self.events.push(item)
            #events will contain all items and monsters and whatnot
    
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.events = Stack()

    def __eq__(self, other):
        """checks equivalence based on ID"""
        #TODO (if i can later) redo this but with type checking
        try: #this is hacky but it works
            if self.id == other.id:
                return True
        except:
            return False
        return False
    
    def __hash__(self):
        """so we can use rooms as dictionary keys"""
        return self.id
    
    def __str__(self):
        """returns the name of the room currently"""
        return self.title

class player():
    def __init__(self):
        self.location = "Void" #will be checked against ID to determine location
        self.inventory = LinkedList()
        self.equipped = {"Hand":"Empty"}

