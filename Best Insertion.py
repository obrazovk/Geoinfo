import math, random
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

# Create the Best Insertion function

def best_insertion(coordinates):
    
    # Set Hamilton circle size as 0

    w = 0

    path = []

    # The list of indexes of all nodes

    numbers = list(range(len(coordinates) - 1))

    # Initialize the circle by 3 nodes

    for i in range(3):

        # Get random choice from the list of indexes

        u = random.choice(numbers)

        # Delete the chosen one from the list of indexes

        numbers.remove(u)

        # Add u to the path

        path.append(u)

        # It will be two nodes after second iteration, the calculate of the distance is now possile

        x1 = coordinates[path[i]][0]
        x2 = coordinates[path[i-1]][0]
        y1 = coordinates[path[i]][1]
        y2 = coordinates[path[i-1]][1]
        if i > 0:
            w_k = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            # Update w
            w = w + w_k

    # Update the size of the circle

    x3 = coordinates[path[0]][0]
    x4 = coordinates[path[2]][0]
    y3 = coordinates[path[0]][1]
    y4 = coordinates[path[2]][1]
    w = w + math.sqrt((x3 - x4)**2 + (y3 - y4)**2)

    # Add the first node

    path.append(path[0])

    # Algorithm Best insertion

    # While the list of indexes is not empty

    while len(numbers) > 0:

        # The shortest distances of the next node will be saved 

        w_min = float("inf")

        # Set position of insertion to the path

        index = - 1

        # Get random choice from the list of indexes

        u = random.choice(numbers)

        # Save the coordinates of the chosen node

        x = coordinates[u][0]
        y = coordinates[u][1]

        # Calculate the distance to identify the insertion position of the chosen node

        for i in range(len(path) - 1):

            # The i-nodes

            z1 = coordinates[path[i]][0]
            z2 = coordinates[path[i]][1]

            # The i+1-nodes

            z3 = coordinates[path[i+1]][0]
            z4 = coordinates[path[i+1]][1]

            # Calculate the distance between chosen node and i_node

            w_k1 = math.sqrt((x - z1)**2 + (y - z2)**2)

            # Calculate the distance between chosen node and i+1-node

            w_k2 = math.sqrt((x - z3)**2 + (y - z4)**2)

            # Calculate the distance between i-node a i+1-node

            w_k3 = math.sqrt((z1 - z3)**2 + (z2 - z4)**2)

            # Calculate the triangle inequality

            w_k4 = w_k1 + w_k2 - w_k3

            # If thew_k4 is smaller than min_w, overwrite min_w

            if w_k4 < w_min:
                w_min = w_k4

                # Set position of insertion to the path 

                index = i + 1

        # Add the distance to the circle size

        w = w + w_min

        # Put the node to the path to the position of insertion

        path.insert(index,u)

        # Delete the chosen one form the list of indexes

        numbers.remove(u)
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


input_file = "C:\\Users\\lucie.krausova\\Desktop\\cr_obce.txt"
#input_file = "C:\\Users\\lucie.krausova\\Desktop\\vrcholy_cr_1000.txt"

# Call the load coordinates function

coordinates = load_coordinates(input_file)

# Call the Best Insertion function

path, w = best_insertion(coordinates)

# Call the Visualization function

visualization(coordinates, path)

print(w)