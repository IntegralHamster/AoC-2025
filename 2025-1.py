with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
position = 50
zero_count = 0

for line in lines:
    if line[0] == 'R':
        position += int(line[1:])
    elif line[0] == 'L':
        position -= int(line[1:])
    position = position % 100
    if position == 0:
        zero_count += 1

print(zero_count)

zero_count = 0
position = 50

# for line in lines:
#     start_position = position
#     if line[0] == 'R':
#         position += int(line[1:])
#     elif line[0] == 'L':
#         position -= int(line[1:])
#     if ((position <= 0 <= start_position) or (start_position <= 100 <= position)) and start_position != 0:
#         zero_count += 1 
#     if (position // 100) > 1:
#         print(start_position, line, position)
#         zero_count += int(line[1])
#     elif (position // 100) < -1:
#         print(start_position, line, position)
#         zero_count += int(line[1])
#     position = position % 100
    
# print(zero_count)

for line in lines:
    if line[0] == 'R':
        for i in range(int(line[1:])):
            position += 1 
            if position == 100:
                zero_count += 1 
                position = 0
    elif line[0] == 'L':
        for i in range(int(line[1:])):
            position -= 1 
            if position == -100 or position == 0:
                zero_count += 1 
                position = 0
        if position < 0:
            position = 100 - abs(position)

print(zero_count)