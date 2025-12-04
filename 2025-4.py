with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
def look_nw(grid,x,y):
    if x == 0 or y == 0:
        return 0
    elif grid[x-1][y-1] == '@':
        return 1
    else:
        return 0

def look_n(grid,x,y):
    if y == 0:
        return 0
    elif grid[x][y-1] == '@':
        return 1
    else:
        return 0

def look_ne(grid,x,y):
    if x > len(grid) - 2 or y == 0:
        return 0
    elif grid[x+1][y-1] == '@':
        return 1
    else:
        return 0

def look_sw(grid, x, y):
    if x == 0 or y > len(grid[0]) - 2:
        return 0
    elif grid[x-1][y+1] == '@':
        return 1
    else:
        return 0

def look_s(grid, x, y):
    if y > len(grid[0]) - 2:
        return 0
    elif grid[x][y+1] == '@':
        return 1
    else:
        return 0

def look_se(grid, x, y):
    if x > len(grid) - 2 or y > len(grid[0]) - 2:
        return 0
    elif grid[x+1][y+1] == '@':
        return 1
    else:
        return 0

def look_w(grid, x, y):
    if x == 0:
        return 0
    elif grid[x-1][y] == '@':
        return 1
    else:
        return 0

def look_e(grid, x, y):
    if x > len(grid) - 2:
        return 0
    elif grid[x+1][y] == '@':
        return 1
    else:
        return 0

cycle_remove = []
while True:
  remove_positions = []
  for j in range(len(lines)):
      for i in range(len(lines[0])):
          if lines[j][i] == '@':
              adj_count = look_nw(lines, j, i) + look_ne(lines, j, i) + look_n(lines, j, i) + look_e(lines, j, i) + look_w(lines, j, i) + look_sw(lines, j, i) + look_se(lines, j, i) + look_s(lines, j, i)
              if adj_count < 4:
                remove_positions.append([j, i])
  cycle_remove.append(len(remove_positions))
  if len(remove_positions) == 0:
    break
  for update_paper in remove_positions:
    if update_paper[1] == 0:
      lines[update_paper[0]] = '.' + lines[update_paper[0]][1:]
    elif update_paper[1] == len(lines[update_paper[0]]) - 1:
      lines[update_paper[0]] = lines[update_paper[0]][0:len(lines[update_paper[0]]) - 1] + '.'
    else:
      lines[update_paper[0]] = lines[update_paper[0]][0:update_paper[1]] + '.' + lines[update_paper[0]][update_paper[1]+1:]

print(cycle_remove[0], sum(cycle_remove))
