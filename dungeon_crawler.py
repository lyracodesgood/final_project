"""
Dungeon Crawler final project - Lyra
"""

from modules.graph import Graph
from modules.stack import Stack
from modules.linked_list import LinkedList
from modules.world import Room, Player, Enemy, Item
from random import randint

#globals -------------------------------------------------------------- globals
keep_going = True #for gameloop

#enemies, used by event handler
goblin = Enemy(
    "Goblin",
    "A small green humanoid with sharp teeth and a bad temper.",
    2,
    1,
    "Spear",
    "AiiIIIIIEEEEEeeeeeeeeeeeeooooOOOOOuuuughhhHHHHHHhhhhh!"
    )

dragon = Enemy(
    "Dragon",
    "A massive crimson beast with four legs and wings.",
    10,
    3,
    "Dragons breath",
    "SscccccccccccraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAaaa!!!"
    )

ratking = Enemy(
    "Rat King Jormungario",
    "A mighty beast writhing with tails and snouts",
    15,
    2,
    "Five-tail whip attack",
    "GRrrrrrrrrruuuuuuuuuuuuuuuuuuuuuuuuaaaaaaaaaaaaaaghhhhh!!!!!"
)


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

visited = Stack() #for remembering our path thru the dungeon
visited.push(entry_chamber) #first room the player exists in

menu = {
    1:"Move to a neighboring room.",
    2:"Observe surroundings",
    3:"Pick up item",
    4:"Show travel history.",
    5:"Show player inventory",
    6:"Use item from inventory"
    }

battle_menu = {
    1:"Cast Fireball at enemy",
    2:"Use item from inventory",
    3:"Attempt to run"
} 

#functions ---------------------------------------------------------- functions

def event_handler(events: Stack):
    """makes enemies in rooms functional"""
    while events.peek() != "Empty":
        event = events.pop()
        #TODO this function
        #battle
        print(f"a {event.name} has ambushed you! Stand and fight!")
        while event.hp > 0:

            print(f"HP: {user.display_hp()}")
            print()
            #player
            player_choice = menu_input(battle_menu)

            match player_choice:
                case 1: #fireball
                    print(f"You cast a mighty Fireball at the {event.name}.")
                    print()

                    dmg = randint(1,5)
                    print(f"You deal {dmg} to the {event.name}.")
                    event.hp -= dmg
                case 2: #use item
                    use_item()
                case 3: #attempt to run
                    coinflip = randint(1,2)
                    if coinflip == 2:
                        print("You run away like a coward.")
                        return
                    print("You fail to escape.")
            
            #enemy
            print()
            coinflip = randint(1,2)
            if coinflip == 2:
                print(f"You are struck by the {event.attack}, taking {event.dmg} damage.")
                user.hp -= event.dmg
            else:
                print(f"The {event.name} misses you with its {event.attack}")

            if user.hp <= 0:
                print()
                print(f"You have been slain by the {event.name}.")
                return
                
        print()
        print(f"You have defeated the {event.name}. Its lets out a terrible screech: {event.deathrattle}!!")
        print()

        for item in event.deathitems:
            user.location.items.append(item.data)
            print(f"The {event.name} drops a {item.data.name} on the ground as it dies.")
            print()
        #if there are items to drop
        


#MENU FUNCTIONS
#1
def move_to_neighbor():
    """lists neighboring rooms based on user location"""
    neighboring_rooms = dungeon.adj_list[user.location] #this is a linked list
    #print(neighboring_rooms) debug
    print()
    print("Choose a room to travel to")
    return neighboring_rooms[menu_input(neighboring_rooms) - 1]

#4
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

#2 observe surroundings
def observe_surroundings():
    print(user.location.description)
    if len(user.location.items) > 0:
        print("items in room: ", end = "")
        count = 0
        for item in user.location.items:
            print(f"{item}", end = "")
            count += 1
            if count != len(user.location.items):
                print(", ", end = "")
#3 pick up item
def pickup_item():
    #TODO make this functional so we can pickup items in rooms
    if user.location.items.head == None:
        print("No items to pick up.")
        return #byeee
    choice = menu_input(user.location.items) #getting which item to grab
    chosen_item = user.location.items.pop(choice - 1).data
    #print(type(chosen_item)) debugs
    user.inventory.append(chosen_item)

#5 Show player inventory
def display_inventory():
    print(user.inventory)


#functions for items
def display_map():
    print(worldmap)

def heal():
    print("You uncap the bright red potion and gulp down the delicious contents.")
    user.hp = 11 #11 so that when it ticks down by one u r still full hp

def bite_coin():
    print("You take one of the gold coins and bite down on it hard... Ouch! It's real!")

def whisper_riddle():
    print("An otherworldy voice whispers in your ear: 42")
    


#special zone for ingame items that have functions attached
game_map = Item("Map", display_map, False)

health_potion = Item("Health Potion", heal, True)

gold_pile = Item("A great number of gold coins", bite_coin, False)

riddle_answer = Item("A small scrap of paper with some writing on it.", whisper_riddle, False)

#adding death items to enemies
goblin.deathitems.append(health_potion)

dragon.deathitems.append(gold_pile)

ratking.deathitems.append(gold_pile)
ratking.deathitems.append(riddle_answer)

#6 option
def use_item():
    if len(user.inventory) == 0:
        print("No items in inventory.")
        return
    print()
    chosen_item_index = menu_input(user.inventory) - 1 #-1 for 0 indexing in pop

    #print(chosen_item_index) debug
    #print(type(user.inventory[chosen_item_index]))
    print()
    user.inventory[chosen_item_index].use()
    if user.inventory[chosen_item_index].onetime: #if its a onetime use
        user.inventory.pop(chosen_item_index)

#PUTTING ITEMS IN ROOMS
entry_chamber.items.append(game_map) #the map in the room
entry_chamber.items.append(health_potion) #the map in the room
treasure_room.items.append(gold_pile) #gold in the treasure room

#PUTTING ENEMIES IN ROOMS

goblin_den.events.push(goblin.copy())
goblin_den.events.push(goblin.copy()) #2 goblins in the den

sewer.events.push(goblin.copy())

old_airship_pad.events.push(goblin.copy())

dragon_obs.events.push(dragon)

rat_kings_chamber.events.push(ratking)

#menus input
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
    print() #whitespace
    match choice:
        case 1:
            user.location = move_to_neighbor()
            visited.push(user.location)
#            while user.location.events.peek() != "Empty":
#                event = user.location.events.pop() #TODO finish this? idk
                
        case 2:
            observe_surroundings()
        case 3:
            pickup_item()
        case 4:
            list_visited()
        case 5:
            print(user.display_inventory())
        case 6:
            use_item()
    return True #everything else

def continue_game():
    """checks if the game should end"""
    if user.hp < 1:
        return False
    return True

#game setup -------------------------------------------------------- game setup
#dungeon.depth_first_traversal(entry_chamber)
#print(type(entry_chamber))

print("        WELCOME TO DYING WIZARD SIMULATOR!")
#game loop ---------------------------------------------------------- game loop
while keep_going:
    print()
    print(f"HP: {user.display_hp()}")
    print(f"Current location: {user.location}")
    print()

    #events in room happen here
    event_handler(user.location.events)
    if user.hp <= 0: #added to handle deaths in battle, better implimentation i possible
        break

    #choose what to do
    menu_choice(menu_input(menu))

    user.hp -= 1 #uh oh
    keep_going = continue_game()