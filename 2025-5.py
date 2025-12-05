import copy

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

fresh_ranges = []
ingridients = []
for line in lines:
  if '-' in line:
    left, right = line.split('-')
    fresh_ranges.append([int(left), int(right)])
  elif line == '':
    continue
  else:
    ingridients.append(int(line))

freshness = 0
for test in ingridients:
  for possibility in fresh_ranges:
    if possibility[0] <= test <= possibility[1]:
      freshness += 1
      break
print(freshness)

supremely_fresh = [fresh_ranges[0]]

for test_fresh in fresh_ranges[1:]:
  change_flag = 0
  for existing_fresh in supremely_fresh:
    if (test_fresh[1] < existing_fresh[0]) or (test_fresh[0] > existing_fresh[1]):
      continue
    elif test_fresh[0] < existing_fresh[0] <= test_fresh[1] <= existing_fresh[1]:
      change_flag = 1
      existing_fresh[0] = test_fresh[0]
      break
    elif test_fresh[0] < existing_fresh[0] <= existing_fresh[1] < test_fresh[1]:
      existing_fresh[0] = test_fresh[0]
      existing_fresh[1] = test_fresh[1]
      change_flag = 1
      break      
    elif existing_fresh[0] <= test_fresh[0] <= test_fresh[1] <= existing_fresh[1]:
      change_flag = 1
      break
    elif existing_fresh[0] <= test_fresh[0] <= existing_fresh[1] < test_fresh[1]:
      change_flag = 1
      existing_fresh[1] = test_fresh[1]
      break
  if change_flag == 0:
    supremely_fresh.append(test_fresh)
    
while True:
  previous_step = copy.deepcopy(supremely_fresh)
  for test_fresh in supremely_fresh:
    change_flag = 0
    for existing_fresh in supremely_fresh:
      if (test_fresh[1] < existing_fresh[0]) or (test_fresh[0] > existing_fresh[1]) or (test_fresh == existing_fresh):
        continue
      elif test_fresh[0] < existing_fresh[0] <= test_fresh[1] <= existing_fresh[1]:
        change_flag = 1
        existing_fresh[0] = test_fresh[0]
        break
      elif test_fresh[0] < existing_fresh[0] <= existing_fresh[1] < test_fresh[1]:
        existing_fresh[0] = test_fresh[0]
        existing_fresh[1] = test_fresh[1]
        change_flag = 1
        break      
      elif existing_fresh[0] <= test_fresh[0] <= test_fresh[1] <= existing_fresh[1]:
        change_flag = 1
        break
      elif existing_fresh[0] <= test_fresh[0] <= existing_fresh[1] < test_fresh[1]:
        change_flag = 1
        existing_fresh[1] = test_fresh[1]
        break
  popping = []
  for test in supremely_fresh:
    if supremely_fresh.count(test) > 1 and test not in popping:
      popping.append(test)
  if len(popping) != 0:
    for test in popping:
      supremely_fresh.remove(test)
  if supremely_fresh == previous_step:
    break
      
freshness_overload = 0
for test_fresh in supremely_fresh:
  freshness_overload += test_fresh[1] - test_fresh[0] + 1
  
print(freshness_overload)
    
      

  
