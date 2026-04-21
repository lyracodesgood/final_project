"""
Dungeon Crawler final project - Lyra
"""

from modules.graph import Graph
from modules.stack import Stack
from modules.world import Room

#globals -------------------------------------------------------------- globals
keep_going = True #for gameloop
visited = Stack() #for remembering our path thru the dungeon
dungeon = Graph() #the graph
#TODO create dungeon here
"""
Entry_Chamber           Secret Treasure Room
     |                    |
   Goblin Den ------ Dragon Observatorium
     |                    |
    Sewer               Delapidated Airship Pad
     |
     Rat King's Chamber
"""
entry_chamber = Room(1,"Entry Chamber","A marble chamber")
goblin_den = Room(2,"Goblin Den",
                   "A marble chamber covered in crude drawings and litter.")
sewer = Room(3, "Sewer",
            "A dank chamber, with a pool of sewage bubbling gently in the middle")
rat_kings_chamber = Room(4, "Rat King's Chamber", "A dark chamber, blood covers the walls.")
treasure_room = Room(5, "Secret reasure Room",
                     "An opulent chamber, wall to cieling gleaming and gold coated.")
dragon_obs = Room(6, "Dragon Observatory",
                  "A room with a domed glass cieling, the dragons are long gone.")
old_airship_pad = Room(7, "Delapidated Airship Pad",
                   "A decaying chamber, a sheer cliff greets you on the opposite side of the room.")

#add vertices
dungeon.add_vertex(entry_chamber)
dungeon.add_vertex(goblin_den)
dungeon.add_vertex(sewer)
dungeon.add_vertex(rat_kings_chamber)
dungeon.add_vertex(treasure_room)
dungeon.add_vertex(dragon_obs)
dungeon.add_vertex(old_airship_pad) #the traversal will only return which room number we get to

"""
Entry_Chamber 1          Secret Treasure Room 5
     |                    |
   Goblin Den 2 ------ Dragon Observatorium 6
     |                    |
    Sewer 3              Delapidated Airship Pad 7
     |
     Rat King's Chamber 4
"""
#add edges
dungeon.add_edge(entry_chamber,goblin_den)
dungeon.add_edge(goblin_den, sewer)
dungeon.add_edge(sewer, rat_kings_chamber)
dungeon.add_edge(goblin_den, dragon_obs)
dungeon.add_edge(dragon_obs, treasure_room)
dungeon.add_edge(dragon_obs, old_airship_pad)

menu = {1:""} #base menu options here, TODO others added dynamically later?

#functions ---------------------------------------------------------- functions
def menu_input(menu, bypass = False):
    """takes nothing, returns a number corresponding to menu choice"""
    if bypass == False:
        for key, value in menu.items():
            print(f"{key}: {value}")
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
            pass
        case 2: #replace 2 with the last option number
            return False
    return True #everything else

#game setup -------------------------------------------------------- game steup
dungeon.depth_first_traversal(entry_chamber)
print(type(entry_chamber))
#game loop ---------------------------------------------------------- game loop
while keep_going:
    keep_going = menu_choice(menu_input(menu))