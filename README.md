Assignment instructions

FINAL PROJECT: Dungeon Navigator (Data Structures)

 

OVERVIEW:

You will design and implement a dungeon navigation system using core data structures. The dungeon will be represented as either a graph or a tree, and the player must traverse it, encounter events, and reach a goal.

 

This project emphasizes traversal algorithms, data organization, and problem solving.




CORE OBJECTIVE:

Model a dungeon using a DATA STRUCTURE and allow a player to navigate through it.




REQUIREMENTS:

 

DUNGEON STRUCTURE (REQUIRED)
You must implement ONE of the following:

 

OPTION A: GRAPH (Recommended)

- Rooms are nodes

- Connections are edges

- Store using:

  - Adjacency list (dictionary of lists)

 

OPTION B: TREE

- Dungeon is hierarchical (like floors/levels)

- Each room has children nodes




ROOM DATA
Each room must store:

- Room ID or name

- Description

- Event type:

  - Enemy

  - Treasure

  - Empty


(Hint: use dictionaries or objects)




TRAVERSAL SYSTEM
Player must move through the dungeon using:

 

GRAPH OPTION:

- Allow movement between connected rooms

- Must implement at least ONE:

  - Breadth-First Search (BFS)

  - Depth-First Search (DFS)

 

TREE OPTION:

- Traverse using:

  - Preorder, Inorder, or Postorder traversal




GAMEPLAY LOOP
Create a looped menu:

 

Show Current Room
Move to Connected Room
View Inventory
Quit



EVENTS SYSTEM
When entering a room:

- Enemy → simple combat

- Treasure → add item to inventory

- Empty → message only




INVENTORY SYSTEM
- Use a LIST or STACK

- Store collected items

- Allow viewing inventory




STACK OR QUEUE USAGE (REQUIRED)
You must implement at least ONE:

 

- STACK:

  - Track player movement (backtracking)

OR

- QUEUE:

  - Used in BFS traversal




MINIMUM REQUIREMENTS:

Your program must include:

- A graph OR tree implementation

- At least 5 rooms (nodes)

- Traversal logic (BFS, DFS, or tree traversal)

- A loop-based menu

- At least one list-based structure

- At least one stack or queue

- Functions to organize code




EXTRA CREDIT (OPTIONAL):

- Implement BOTH BFS and DFS

- Shortest path finding

- Weighted graph (different difficulty rooms)

- Save/load dungeon

- Use classes for Node, Graph, Player

- Add boss room with special conditions