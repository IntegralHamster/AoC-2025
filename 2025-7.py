with open('input.txt') as f:
    lines = [list(line.strip().replace('S','1').replace('.','0')) for line in f.readlines()]

split_count1 = split_count2 = 0
for y in range(1, len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] != '^':
      if lines[y-1][x] != '^':
        lines[y][x] = str(int(lines[y][x]) + int(lines[y-1][x]))
    else:
      if lines[y-1][x] != '0':
        split_count1 += 1
        lines[y][x-1] = str(int(lines[y][x-1]) + int(lines[y-1][x]))
        lines[y][x+1] = str(int(lines[y][x+1]) + int(lines[y-1][x]))
  if y == len(lines) - 1:
    for x in range(len(lines[y])):
      split_count2 += int(lines[y][x])
      
print(split_count1, split_count2)
