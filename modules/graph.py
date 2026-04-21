"""a graph class by lyra
implemented through the use of an adjacency list
"""

from modules.linked_list import LinkedList
from modules.stack import Stack
from modules.queue import Queue

class Graph():
    def __init__(self):
        self.adj_list = {} 
    
    def add_vertex(self, data):
        """adds a linked list to the end of the adjacency list"""
        self.adj_list[data]=LinkedList()

    def add_edge(self, vert_a_data, vert_b_data): 
        """adds un undirected, unweighted edge between two vertices"""
        #can be signifigantly refactored, simply add vert_a to vert_b adjacency list and vice versa
        #TODO refactor as said above, but also make it add the vertices if they do not exist

        found = 0 #for early breaking
        for vertex, l_list in self.adj_list.items(): #l_list is the linked list
            if vertex == vert_a_data: 
                #if we find vertex a, append a node representing vertex b
                l_list.append(vert_b_data)
                found += 1

            elif vertex == vert_b_data:
                #if we find b, append a
                l_list.append(vert_a_data)
                found += 1

            if found >= 2:
                break
    
    def display_graph(self):
        #TODO make this prettier
        for vertex, l_list in self.adj_list.items():
            print(f"{vertex} - connected to: ", end = "")
            count = 0
            for item in l_list:
                if count < l_list.length() - 1:
                    print(f"{item}, ", end = "")
                else:
                    print(f"{item} ", end = "")
                count += 1
            print()

    def is_neighbor(self, vert_a_data, vert_b_data):
        """returns true if two locations are nieghbors, false otherwise"""
        #assuming this means is an edge for now, because thats easier than path
        l_list_a = None
        l_list_b = None
        for l_list in self.adj_list.values():
            #print(l_list)
            if l_list.head.data == vert_a_data:
                #print(l_list)
                #check if b is in this list now
                for cur_node in l_list:
                    if cur_node.data == vert_b_data:
                        return True
                break
        
        for l_list in self.adj_list.values():
            if l_list.head.data == vert_b_data:
                #print(l_list)
                for cur_node in l_list:
                    if cur_node.data == vert_a_data:
                        return True
                break
        
        #welp didnt find a connection
        return False
    
    def is_connected(self, start, target):
        """start at a node, ,traverse the graph till you find the target,
        return true if you find, otherwise return false"""
        visited = {} #gonna try a list today (4/14)
        for vertex in self.adj_list.keys():
            visited[vertex] = False

        #lets get traversing
        adjacent = Stack()
        adjacent.push(start)

        while adjacent.peek() != "Empty":
            cur_vertex = adjacent.pop()
            visited[cur_vertex] = True

            if cur_vertex == target:
                return True #the only difference from the traversal functions

            for vertex, l_list in self.adj_list.items():
                if vertex == cur_vertex:
                    for item in l_list:
                        if not visited[item.data]:
                            adjacent.push(item.data) #gathering nodes
                            visited[item.data] = True
                    break


        return False
    
    def depth_first_traversal(self, start_vertex):
        #we must first mark all the vertices as unvisited
        visited = {} #im using a dictionary because it makes sense to me
        for vertex in self.adj_list.keys():
            visited[vertex] = False 

        #now we need to add the start node to the stack
        adjacent = Stack()
        adjacent.push(start_vertex)

        #now we recurse with a while loop
        while adjacent.peek() != "Empty":
            cur_vertex = adjacent.pop()
            visited[cur_vertex] = True #mark our visit
            #print(f"current vertex: {cur_vertex}") #debug
            print(f"vertex: {cur_vertex}")
            #lets get the adjacent nodes
            for vertex, l_list in self.adj_list.items():
                if vertex == cur_vertex:
                    #here is where we actually add in the nodes
                    for item in l_list:
                        if not visited[item.data]:
                            adjacent.push(item.data)
                            visited[item.data] = True #idk if this should go here?
                            #print(f"pushing: {item.data}") #debug
                    break
            #print(adjacent) #debug

    def breadth_first_traversal(self, start_vertex):

        #mark all vertices unvisited
        visited = {}
        for vertex in self.adj_list.keys():
            visited[vertex] = False

        adjacent = Queue()
        adjacent.enqueue(start_vertex) #start with da start

        while adjacent.peek() != "Empty":
            cur_vertex = adjacent.dequeue()
            visited[cur_vertex] = True #mark visit
            print(f"vertex: {cur_vertex}")

            #grab adjacent
            for vertex, l_list in self.adj_list.items():
                if vertex == cur_vertex: #if its the one we are on rn
                    for item in l_list:
                        if not visited[item.data]:  #check if neighbor has been visited
                            adjacent.enqueue(item.data)
                            visited[item.data] = True
                    break

    def count_neighbors(self, target_vertex):
        for vertex, l_list in self.adj_list.items():
            if  vertex == target_vertex:
                count = 0
                for item in l_list:
                    count += 1
                return count

