with open('input.txt') as f:
    lines = [line for line in f.readlines()]

points = []
for i in range(len(lines)):
  x,y = lines[i].split(',')
  points.append([int(x), int(y)])
  
def area(corner1, corner2):
  return (abs(corner1[0] - corner2[0]) + 1)*((abs(corner1[1] - corner2[1]) + 1))

areas = []
max_area = 0
for i in range(len(lines)):
  for j in range(i, len(lines)):
    if i != j:
      area
      areas.append([[i,j], area(points[i], points[j])])
      if area(points[i], points[j]) > max_area:
        max_area = area(points[i], points[j])

print(max_area)
areas = sorted(areas, key = lambda x: x[1], reverse = True)
points = sorted(points, key = lambda x: (x[0], x[1]))
x_values = {}
y_values = {}
for point in points:
  if point[0] in x_values.keys():
    x_values[point[0]] += 1
  else:
    x_values[point[0]] = 1
  if point[1] in y_values.keys():
    y_values[point[1]] += 1
  else:
    y_values[point[1]] = 1
    
print(max(x_values.values()), max(y_values.values())) # 2 2 means that we can just connect the only ones with that x/y coordinate without extra checks

vertices = []
last_corner_index = 0
x_y_flip = 0
while len(vertices) < len(points):
  for i in range(len(points)):
    if i != last_corner_index and points[last_corner_index][x_y_flip] == points[i][x_y_flip]:
      vertices.append([last_corner_index, i])
      x_y_flip = 1 - x_y_flip
      last_corner_index = i
      break

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
  
i = 0
while True:
  intersect_flag = False
  for vertice in vertices:
    end1 = points[vertice[0]]
    end2 = points[vertice[1]]
    test_end1 = points[areas[i][0][0]]
    test_end2 = points[areas[i][0][1]]
    test_end3 = [test_end1[0], test_end2[1]]
    test_end4 = [test_end2[0], test_end1[1]]
    if areas[i][0][0] in vertice or areas[i][0][1] in vertice:
      continue
    if intersect(end1, end2, test_end1, test_end3) or intersect(end1, end2, test_end2, test_end3) or (intersect(end1, end2, test_end1, test_end4) or intersect(end1, end2, test_end2, test_end4)):
      intersect_flag = True
      break
  if intersect_flag:
    i += 1
    if i % 1000 == 0:
      print(100*i/len(areas))
    continue
  else:
    print(i, areas[i][1])
    break

# part 2 doesn't work
