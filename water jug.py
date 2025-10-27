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
            (cap1, b),  # Fill Jug1
            (a, cap2),  # Fill Jug2
            (0, b),     # Empty Jug1
            (a, 0),     # Empty Jug2
            (max(a - (cap2 - b), 0), min(cap2, a + b)),  # Pour Jug1 → Jug2
            (min(cap1, a + b), max(b - (cap1 - a), 0))   # Pour Jug2 → Jug1
        ])

cap1, cap2, target = 4, 3, 2
print("Steps to reach target:")
water_jug(set(), cap1, cap2, target)
