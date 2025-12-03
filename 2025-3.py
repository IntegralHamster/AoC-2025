with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
def joltage1(batteries):
    
    maximum = max(batteries)
    if batteries.index(maximum) == len(batteries) - 1:
        return maximum + 10*max(batteries[0:len(batteries)-1])
    else:
        return 10*maximum + max(batteries[batteries.index(maximum) + 1:])
 
def joltage2(batteries, ans_length):
  
  if ans_length == 0:
    return ''
  
  maximum = max(batteries)
  max_pos = batteries.index(maximum)
  length = len(batteries)
  
  if len(batteries) == ans_length:
    return ''.join(str(y) for y in batteries)
  elif len(batteries[max_pos+1:]) >= ans_length - 1:
    return str(maximum) + ''.join(str(z) for z in joltage2(batteries[max_pos+1:], ans_length - 1))
  else:
    return joltage2(batteries[0:max_pos], ans_length - 1 - len(batteries[max_pos+1:])) + ''.join(str(y) for y in batteries[max_pos:])
    
total_jolt1 = 0  
total_jolt2 = 0 
for line in lines:
    battery_line = [int(x) for x in line]
    total_jolt1 += joltage1(battery_line)
    total_jolt2 += int(joltage2(battery_line, 12))
    
print(total_jolt1, total_jolt2)
