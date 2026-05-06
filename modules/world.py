"""a file containing classes for the dungeon crawler, like player and room"""
from modules.stack import Stack
from modules.linked_list import LinkedList


class Room():

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.events = Stack()
        self.items = LinkedList()

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

class Player():
    def __init__(self, room):
        self.location = room #will be checked against ID to determine location
        self.inventory = LinkedList()
        self.hp = 10
        self.mp = 10
        
    def pickup(self, item):
        self.inventory.append(item)
    
    def display_inventory(self):
        """returns the items in inventory in string form, otherwise returns empty"""
        if len(self.inventory) == 0:
            return "Inventory empty."

        r_str = ""
        for item in self.inventory:
            r_str =  r_str + str(item)
            if item.next == None:
                break
            r_str = r_str + ", "
        return r_str
    
    def display_hp(self):
        """returns a string representation of hp"""
        return f"[{str("<3" * self.hp)}{str(" x" * (10 - self.hp))}]" 
    
    def display_mp(self):
        """returns a string representation of mana"""
        return f"[{str("~*" * self.mp)}{str("  " * (10 - self.mp))}]" 

class Enemy():
    def __init__(self, name, description, hp, dmg, deathrattle):
        self.name = name
        self.description = description
        self.hp = hp
        self.dmg = dmg
        self.deathrattle = deathrattle

class Item():
    def __init__(self, name, func:function, onetime:bool):
        self.name = name
        self.func= func
        self.onetime = onetime

    def __str__(self):
        """returns the string representation of the item, the name"""
        return self.name
    
    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def use(self):
        """uses the item"""
        self.func()


