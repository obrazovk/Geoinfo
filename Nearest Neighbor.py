import math
from matplotlib import pyplot

# Reading .txt file and saving coordinates to the list

input_file = "C:\\Users\\lucie.krausova\\Desktop\\vrcholy_cr_1000.txt"
coordinates = []
with open(input_file) as f:
   lines = f.readlines()
   for line in lines:
       line = line[:-2]
       line = line.split(";") 
       line[0] = float(line[0])
       line[1] = float(line[1])
       coordinates.append(line)

# Status of all nodes as unprocessed

s = ["N"] * (len(coordinates))
w = 0  
start = 0 
s[0] = "C" 
path = [start]

# Algorithm Nearest Neighbor

while "N" in s:
    min_w = float("inf")
    u = - 1
    x1 = coordinates[path[-1]][0]
    y1 = coordinates[path[-1]][1]
    for i in range(1, len(coordinates)): 
        if s[i] == "N":
            x2 = coordinates[i][0]
            y2 = coordinates[i][1]
            w_i = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if w_i < min_w:
                min_w = w_i
                u = i
    path.append(u)
    s[u] = "C"
    w = w + min_w
x3 = coordinates[0][0]
y3 = coordinates[0][1]
x4 = coordinates[path[-1]][0]
y4 = coordinates[path[-1]][1]
w = w + math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
path.append(path[0])

# Vizualization

x = []
y = []
for i in path:
    x.append(coordinates[i][0])
    y.append(coordinates[i][1])

x_nodes = []
y_nodes = []
for c in coordinates:
    x_nodes.append(c[0])
    y_nodes.append(c[1])

pyplot.scatter(x_nodes, y_nodes, c = "blue")
pyplot.plot(x, y, c = "red")
pyplot.show()

print(w)