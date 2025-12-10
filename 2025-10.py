with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

lights = []
buttons = []
joltages = []
for line in lines:
  a,b = line.split('] (')
  lights.append(a.replace('[','').replace('.','0').replace('#', '1'))
  c,d = b.split(') {')
  joltages.append([int(f) for f in d.replace('}','').split(',')])
  h = []
  for e in c.split(') ('):
    h.append(e.split(','))
  buttons.append(h)


def testing(lights_in, buttons_in):
  min_presses = 99
  for j in range(pow(2, len(buttons_in))):
    binary_j = '0'*(len(bin(pow(2, len(buttons_in)))[2:]) - len(bin(j)[2:]) - 1) + bin(j)[2:]
    presses = binary_j.count('1')
    if presses < min_presses:
      correct = {}
      for i in range(len(lights_in)):
        correct[i] = int(lights_in[i])
      for flip in range(len(binary_j)):
        if binary_j[flip] == '1':
          for button in buttons_in[flip]:
            correct[int(button)] = 1 - correct[int(button)]
      if 1 not in correct.values():
        min_presses = presses
  return min_presses
        
total_presses = 0
for i in range(len(lines)):
  total_presses += testing(lights[i], buttons[i])
  
print(total_presses) # part 1 only
