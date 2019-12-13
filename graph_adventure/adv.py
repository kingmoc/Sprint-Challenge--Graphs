from room import Room
from player import Player
from world import World

from random import randrange
from util import Stack, Queue

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# roomGraph={0: {'n': 1}, 1: {'s': 0, 'n': 2}, 2: {'s': 1}}
roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)

def bfs(start, traversal_graph):
    q = Queue()
    q.enqueue([start])
    visited = set()
    blank = []
    
    while q.size() > 0:
        print('IN BFS WHILE')
        path = q.dequeue()
        v = path[-1]
        print(v,'v from bfs')
        
        if v not in visited:
            # if traversal_graph[v] == dest: 
            #     return path
            for dir_ in traversal_graph[v]:
                print(dir_, 'ITEM IN TRAVERSAL GRAPH FROM BFS')
                if traversal_graph[v][dir_] == '?':
                    return blank
                visited.add(v)

            for direction, node in traversal_graph[v].items():
                blank.append(direction)
                copy_path = path.copy()
                copy_path.append(node)
                print(path, 'path')
                print(blank, 'path back to unexplored')
                q.enqueue(copy_path)

traversalPath = []
opposite = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

s = Stack()
s.push(0)
visited = []
t_graph={}

while s.size() > 0:
    print('in while')
    v = s.pop()
    
    if v not in visited:
        print(v, 'current node')
        exits = player.currentRoom.getExits()
        print(exits, 'exits')
        
        t_graph[v] = {}
        print(traversalPath, 'paths as they build')        
        for i in range(len(exits)):
            t_graph[v][exits[i]] = '?'
            # print(t_graph,'erererererer')
        
        if len(traversalPath) > 0:
            last_dir = traversalPath[-1]
            opposite[last_dir]
            t_graph[v][opposite[last_dir]] = visited[-1]
        
        print(t_graph, 'traversal graph')
        unexplored = []
        for key,value in t_graph[v].items():
            if value == '?':
                unexplored.append(key)
        print(unexplored, 'unexplored')
        if len(unexplored) != 0:
            next_dir = unexplored[randrange(len(unexplored))]
            print(next_dir, 'next_dir QWEWQEE')
            
            traversalPath.append(next_dir)
            player.travel(next_dir)
            t_graph[v][next_dir] = player.currentRoom.id
        else:
            print('IN ELSE!!!!!!!!')
            dir_to_unexplored = bfs(player.currentRoom.id, t_graph)
            dir_to_unexplored.pop()
            for new_dir in dir_to_unexplored:
                print(new_dir, 'dfadfadfadsfasdfasdfadfadfasdfasdfadfafdfadfadfafadf')

        visited.append(v)
        s.push(player.currentRoom.id)

# This is where to begin the BFS search on nearest unexplored room



print(t_graph, 'traversal graph')
print(visited, 'visited')
print(traversalPath, 'Directions Traveled - FINAL')

# print(player.travel('n'))
# print(player.currentRoom.id)
# print(player.currentRoom.getExits())
'''
roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
'''
# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
