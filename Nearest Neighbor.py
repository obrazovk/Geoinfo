import math
from matplotlib import pyplot

# Reading .txt file and saving coordinates to the list

def load_coordinates(input_file):
    coordinates = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-2]
            line = line.split(";") 
            line[0] = float(line[0])
            line[1] = float(line[1])
            coordinates.append(line)
    return coordinates

# Create the Nearest Neighbor function

def nearest_neighbor(coordinates):

    # Status of all nodes as unprocessed

    s = ["N"] * (len(coordinates))

    # Set Hamilton circle size as 0

    w = 0  

    # Index of the first node

    start = 0 

    # Set first node as closed

    s[0] = "C" 

    # Create path that starts at first node

    path = [start]

    # Algorithm Nearest Neighbor

    # Exists while node with setting unprocessed exists 

    while "N" in s:

        # The shortest distances of the next node will be saved 

        min_w = float("inf")

        # Index of the nearest node

        u = - 1

        # The last node

        x1 = coordinates[path[-1]][0]
        y1 = coordinates[path[-1]][1]

        # Go through node to node

        for i in range(1, len(coordinates)): 

            # If node is unprocessed

            if s[i] == "N":

                # The i-node

                x2 = coordinates[i][0]
                y2 = coordinates[i][1]

                # Calculate distance between the last node and the i-node

                w_i = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                # If w_i will be smaller than min_w, overwrite min_w and mark the index of the node

                if w_i < min_w:
                    min_w = w_i
                    u = i

        # Add the nearest node to the path

        path.append(u)

        # Set u as closed

        s[u] = "C"

        # Update w 

        w = w + min_w

    # The last node 

    x3 = coordinates[0][0]
    y3 = coordinates[0][1]

    # The first node

    x4 = coordinates[path[-1]][0]
    y4 = coordinates[path[-1]][1]

    # Update the size of the circle

    w = w + math.sqrt((x3 - x4)**2 + (y3 - y4)**2)

    # Add the first node

    path.append(path[0])
    return path, w

# Create a Vizualization function

def visualization(coordinates, path):

    # The visualization of the path

    x = []
    y = []
    for i in path:
        x.append(coordinates[i][0])
        y.append(coordinates[i][1])

    # The visualization of the nodes

    x_nodes = []
    y_nodes = []
    for c in coordinates:
        x_nodes.append(c[0])
        y_nodes.append(c[1])

    pyplot.scatter(x_nodes, y_nodes, c = "blue")
    pyplot.plot(x, y, c = "red")
    pyplot.show()


#input_file = "C:\\Users\\lucie.krausova\\Desktop\\vrcholy_cr_1000.txt"
input_file = "C:\\Users\\lucie.krausova\\Desktop\\cr_obce.txt"

# Call the load coordinates function

coordinates = load_coordinates(input_file)

# Call the Nearest Neighbor function

path, w = nearest_neighbor(coordinates)

# Call the Visualization function 

visualization(coordinates, path)

print(w)