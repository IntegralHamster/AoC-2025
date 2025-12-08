with open('input.txt') as f:
    lines = [line for line in f.readlines()]

boxes = {}
for i in range(len(lines)):
  x,y,z = lines[i].split(',')
  boxes[i] = [int(x), int(y), int(z)]
  
def distance (box1, box2):
  return pow((box1[0] - box2[0]),2) + pow((box1[1] - box2[1]),2) + pow((box1[2] - box2[2]),2)

lengths = []
for i in range(len(lines)):
  for j in range(i, len(lines)):
    if i != j:
      lengths.append((distance(boxes[i], boxes[j]) ,[i, j]))

def connecting(subgraph, vertice):
  l, r = vertice[0], vertice[1]
  l_index = r_index = -1
  for i in range(len(subgraph)):
    if l in subgraph[i]:
      l_index = i
    if r in subgraph[i]:
      r_index = i
    if r_index != -1 and l_index != -1:
      break
  if r_index == l_index:
    return
  else:
    subgraph.append(subgraph[l_index] + subgraph[r_index])
    remove1, remove2 = subgraph[l_index], subgraph[r_index]
    subgraph.remove(remove1)
    subgraph.remove(remove2)
    return

vertice_count = 1000 # put the required number here, it's 10 for example
lengths = sorted(lengths, key = lambda x: x[0])
subgraphs = [[x] for x in range(len(lines))]

for i in range(vertice_count):
  connecting(subgraphs, lengths[i][1])
  
subgraphs = list(reversed(sorted(subgraphs, key = len)))
print(len(subgraphs[0])*len(subgraphs[1])*len(subgraphs[2]))

while True:
  i += 1
  connecting(subgraphs, lengths[i][1])
  if len(subgraphs) == 1:
    break
    
print(boxes[lengths[i][1][0]][0]*boxes[lengths[i][1][1]][0])
