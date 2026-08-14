from collections import deque

def water_jug_problem(x, y, z):
    queue = deque([(0, 0, [])])
    visited  =  set()
    while queue:
        a, b, steps = queue.popleft()
        if (a, b) in visited: continue
        visited.add((a,b))
        if a==z or b==z: return steps
        queue.append((x, b, steps + ['Fill Jug 1']))
        queue.append((a, y, steps + ['Fill Jug 2']))
        queue.append((0, b, steps + ['Empty Jug 1']))
        queue.append((a, 0, steps + ['Empty Jug 2']))
        amt =  min(a, y - b)
        queue.append((a -  amt, b +  amt, steps + ['Pour Jug 1 into Jug 2']))
        amt=min(x-a, b)
        queue.append((a + amt, b - amt, steps + ['Pour Jug 2 into Jug 1 ']))
    return None

steps = water_jug_problem(4, 3, 2)
if steps:
    print('\n'.join(steps))
else:
    print('No solution found.')
