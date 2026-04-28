"""
Dungeon Crawler final project - Lyra
"""

from modules.graph import Graph
from modules.stack import Stack
from modules.linked_list import LinkedList
from modules.world import Room, Player

#globals -------------------------------------------------------------- globals
keep_going = True #for gameloop
visited = Stack() #for remembering our path thru the dungeon


dungeon = Graph() #the graph
worldmap = """
o----------------------------------------------------o
|                                             n      |
|   Entry_Chamber      Treasure Room        e + w    |
|     |                    |                  s      |
|   Goblin Den ------ Dragon Observatorium           |
|     |                    |                         |
|    Sewer               Delapidated Airship Pad     |
|       \                 /                          |
|       Rat King's Chamber                           |
|                                                    |
o----------------------------------------------------o""" #54 wide, 10 high

entry_chamber = Room(
    1,
    "Entry Chamber",
    "A marble chamber"
    )

visited.push(entry_chamber)

goblin_den = Room(
    2,
    "Goblin Den",
    "A marble chamber covered in crude drawings and litter."
    )
sewer = Room(
    3,
    "Sewer",
    "A dank chamber, with a pool of sewage bubbling gently in the middle"
    )
rat_kings_chamber = Room(
    4,
    "Rat King's Chamber", 
    "A dark chamber, blood covers the walls."
    )
treasure_room = Room(
    5,
    "Secret reasure Room",
    "An opulent chamber, wall to cieling gleaming and gold coated."
    )
dragon_obs = Room(
    6, 
    "Dragon Observatory",
    "A room with a domed glass cieling, the dragons are long gone."
    )
old_airship_pad = Room(
    7,
    "Delapidated Airship Pad",
    "A decaying chamber, a sheer cliff greets you on the opposite side of the room."
    )

#add vertices
dungeon.add_vertex(entry_chamber)
dungeon.add_vertex(goblin_den)
dungeon.add_vertex(sewer)
dungeon.add_vertex(rat_kings_chamber)
dungeon.add_vertex(treasure_room)
dungeon.add_vertex(dragon_obs)
dungeon.add_vertex(old_airship_pad)

#add edges
dungeon.add_edge(entry_chamber,goblin_den)
dungeon.add_edge(goblin_den, sewer)
dungeon.add_edge(sewer, rat_kings_chamber)
dungeon.add_edge(goblin_den, dragon_obs)
dungeon.add_edge(dragon_obs, treasure_room)
dungeon.add_edge(dragon_obs, old_airship_pad)
dungeon.add_edge(old_airship_pad, rat_kings_chamber)

user = Player(entry_chamber)

menu = {1:"Move to a neighboring room.",
        2:"Show travel history."} #base menu options here, TODO others added dynamically later?


#functions ---------------------------------------------------------- functions

#1
def move_to_neighbor():
    """lists neighboring rooms based on user location"""
    neighboring_rooms = dungeon.adj_list[user.location] #this is a linked list
    #print(neighboring_rooms) debug
    print()
    print("Choose a room to travel to")
    return neighboring_rooms[menu_input(neighboring_rooms) - 1].data #.data to extract from node

#2
def list_visited():
    journey = Stack() #holds the reversed history
    while visited.peek() != "Empty":
        room = visited.pop()
        if visited.peek() != "Empty":
            print(str(room), end = " < ")
        else:
            print(str(room))
        journey.push(room)
    
    #now we refill
    while journey.peek() != "Empty":
        visited.push(journey.pop())

#menus
def menu_input(menu, bypass = False):
    """returns a number corresponding to menu choice, now for more iterables!"""
    if bypass == False:
        if type(menu) == dict:
            for key, value in menu.items():
                print(f"{key}: {value}")
        else:
            count = 1
            for item in menu:
                print(f"{count}: {item}")
                count +=1
    choice = input("Choose a number: ")
    
	#input handling
    try:
        choice = int(choice)
    except:
        print("Error: Input not accepted... ", end = "")
        return menu_input(menu, bypass = True) #i recurse thee
    
    if choice > len(menu):
        print("Error: Input out of bounds... ", end = "")
        return menu_input(menu, bypass = True)
    
    return choice

def menu_choice(choice):
    """takes a number choice, executes functions corresponding to 
    the menu choices available, returns true or false to keep going or not"""
    match choice:
        case 1:
            user.location = move_to_neighbor()
            visited.push(user.location)

            while user.location.events.peek() != "Empty":
                event = user.location.events.pop() #TODO finish this? idk
                event()
        case 2:
            list_visited()
    return True #everything else

def continue_game():
    """checks if the game should end"""
    if user.hp < 1:
       return False
    return True

#game setup -------------------------------------------------------- game setup
#dungeon.depth_first_traversal(entry_chamber)
#print(type(entry_chamber))

print("        WELCOME TO DYING WIZARD SIMULATOR!", end = "")
#game loop ---------------------------------------------------------- game loop
while keep_going:
    #print(f"HP: {user.display_hp()} MP: {user.display_mp()}")
    print()
    menu_choice(menu_input(menu))
    

    user.hp -= 1 #better go fast

    #end loop evalutations
    keep_going = continue_game()