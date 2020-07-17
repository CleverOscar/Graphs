from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# Stack for DFS

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.appen(item)

    def pop(self, item):
        if self.stack > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Traversal throught path

class TraversalGraph():
    def __init__(self):
        self.rooms = {}

    def add_room(self, id, exits):
        # Creates an entrance
        directions = {}

        for direction in exits:
            directions[direction] = '?'

        self.rooms[id] = directions

    def get_rear_directon(self, direction):
        if direction == 'n':
            return 's'
        if direction == 's':
            return 'n'
        if direction == 'w':
            return 'e'
        if direction == 'e':
            return 'w'


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
