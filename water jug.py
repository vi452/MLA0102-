from collections import deque

def water_jug(visited, cap1, cap2, target):
    q = deque()
    q.append((0, 0))
    while q:
        a, b = q.popleft()
        if (a, b) in visited:
            continue
        print(f"({a}, {b})")
        visited.add((a, b))
        if a == target or b == target:
            print("Target Reached!")
            return
        q.extend([
            (cap1, b),  
            (a, cap2),  
            (0, b),     
            (a, 0),     
            (max(a - (cap2 - b), 0), min(cap2, a + b)), 
            (min(cap1, a + b), max(b - (cap1 - a), 0))  
        ])
cap1, cap2, target = 4, 3, 2
print("Steps to reach target:")
water_jug(set(), cap1, cap2, target)


output:
Steps to reach target:
(0, 0)
(4, 0)
(0, 3)
(4, 3)
(1, 3)
(3, 0)
(1, 0)
(3, 3)
(0, 1)
(4, 2)
Target Reached!

