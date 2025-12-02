with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
ranges = lines[0].split(',')

def range_check1(test_range):
    badness = 0
    left, right = test_range.split('-')
    for j in range(int(left), int(right) + 1):
        i = str(j)
        if len(i) % 2 == 0:
            half = len(i) // 2
            if i[0:half] == i[half:]:
                badness += int(i)
    return badness

def range_check2(test_range):
    badness = 0
    left, right = test_range.split('-')
    for j in range(int(left), int(right) + 1):
        i = str(j)
        for segment_length in range(1, (len(i) // 2) + 1):
            if i[0:segment_length] * (len(i) // segment_length) == i and segment_length != len(i):
                badness += int(i)
                break
    return badness
    
total_badness1 = 0
total_badness2 = 0
for shelf in ranges:
    total_badness1 += range_check1(shelf)
    total_badness2 += range_check2(shelf)
    
print(total_badness1, total_badness2)
