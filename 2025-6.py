with open('input.txt') as f:
    lines = [line for line in f.readlines()]

lines_updated = []
for line in lines:
  lines_updated.append(line.split())
  
total_p1 = 0  
for i in range(len(lines_updated[0])):
  if lines_updated[-1][i] == '+':
    vertical_total = 0
    for j in range(len(lines_updated)-1):
      vertical_total += int(lines_updated[j][i])
  elif lines_updated[-1][i] == '*':
    vertical_total = 1
    for j in range(len(lines_updated)-1):
      vertical_total *= int(lines_updated[j][i])
  total_p1 += vertical_total

lines_updated2 = []
for i in range(len(lines[0])):
  vertical = ''
  if '\n' == lines[0][i]:
    break
  for j in range(len(lines)-1):
    vertical += lines[j][i]
  lines_updated2.append(vertical.replace(' ', ''))
  
total_p2 = 0  
j = -1
for i in range(len(lines_updated[0])):
  if lines_updated[-1][i] == '+':
    horizontal_total = 0
    while True:
      j += 1
      if j == len(lines_updated2):
        break
      elif lines_updated2[j] == '':
        break
      else:
        horizontal_total += int(lines_updated2[j])
        
  elif lines_updated[-1][i] == '*':
    horizontal_total = 1
    while True:
      j += 1
      if j == len(lines_updated2):
        break
      elif lines_updated2[j] == '':
        break
      else:
        horizontal_total *= int(lines_updated2[j])
  total_p2 += horizontal_total
  
print(total_p1, total_p2)
