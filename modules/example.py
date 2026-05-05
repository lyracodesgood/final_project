"""trying to pass a function as an argument to a construtor and then call it later"""

class Item():
    def __init__(self, name, func:function):
        self.name = name
        self.func = func

    def call_function(self):
        self.func()

def exampe_function():
    print("it worked!")
    print("it really did")

if __name__ == "__main__":

    thing = Item("Thing", exampe_function)

    thing.call_function()