import math, random
from matplotlib import pyplot

# Reading .txt file and saving coordinates to the list

input_file = "C:\\Users\\lucie.krausova\\Desktop\\cr_obce.txt"
#input_file = "C:\\Users\\lucie.krausova\\Desktop\\vrcholy_cr_1000.txt"
coordinates = []
with open(input_file) as f:
   lines = f.readlines()
   for line in lines:
       line = line[:-2]
       line = line.split(";") 
       line[0] = float(line[0])
       line[1] = float(line[1])
       coordinates.append(line)

# Creating an circuit

w = 0
path = []
numbers = list(range(len(coordinates) - 1))
for i in range(3):
    u = random.choice(numbers)
    numbers.remove(u)
    path.append(u)
    x1 = coordinates[path[i]][0]
    x2 = coordinates[path[i-1]][0]
    y1 = coordinates[path[i]][1]
    y2 = coordinates[path[i-1]][1]
    if i > 0:
        w_k = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        w = w + w_k
x3 = coordinates[path[0]][0]
x4 = coordinates[path[2]][0]
y3 = coordinates[path[0]][1]
y4 = coordinates[path[2]][1]
w = w + math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
path.append(path[0])

# Algorithm Best insertion

while len(numbers) > 0:
    w_min = float("inf")
    index = - 1
    u = random.choice(numbers)
    x = coordinates[u][0]
    y = coordinates[u][1]
    for i in range(len(path) - 1):
        z1 = coordinates[path[i]][0]
        z2 = coordinates[path[i]][1]
        z3 = coordinates[path[i+1]][0]
        z4 = coordinates[path[i+1]][1]
        w_k1 = math.sqrt((x - z1)**2 + (y - z2)**2)
        w_k2 = math.sqrt((x - z3)**2 + (y - z4)**2)
        w_k3 = math.sqrt((z1 - z3)**2 + (z2 - z4)**2)
        w_k4 = w_k1 + w_k2 - w_k3
        if w_k4 < w_min:
            w_min = w_k4
            index = i + 1
    w = w + w_min
    path.insert(index,u)
    numbers.remove(u)

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
