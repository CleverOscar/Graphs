'''

Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4


Describe the problem in terms of Graphs
Nodes: 1s
edge: connected n/s/w/e

islands: connected components

Build our graph or just define getNeighbors()

visited = set((0,1))

implementation
# iterate through the matrix
# When we see a 1, it it's not been visted
# increment out islands counter
# run a traversal
# mark things as visited
'''



def get_neighbors(node, matrix):
    row, col = node

    stepNorth = stepSouth = stepWest = stepEast = False
    ## take a step north
    if row > 0:
        stepNorth = True
    ## take a step south
    if row < len(matrix) - 1:
        stepSouth = row + 1
    ## take a step east
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    ## take a step west
    if col > 0:
        stepWest = col - 1

    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))


    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))

    if stepWest is not False and matrix[stepWest][row] == 1:
        neighbors.append((stepWest, row))

    if stepEast is not False and matrix[stepEast][row] ==1:
        neighbors.append((stepEast, row))

def dft_recursive(node, visited, matrix):
    # if node not visited
    if node not in visted
        # add to visied
        visied.add(node)

        # get neighbors
        neighbors = get_neighbors(node, matrix)

        # for each neighbor
        for neighbor in neighbors:
        #   recurse
            dft_recursive(neighbor, visited, matrix)





def island_counter(islands):
    visited = set()

    number_islands = 0

    # iterate through the matrix
    for row in range(len(islands[row])):
        node = (row, col)
    # When we see a 1, it it's not been visted
        if node not in visited and islands[row][col] == 1
            # increment out islands counter
            number_islands += 1
            # run a traversal
            dft_recursive(node)
