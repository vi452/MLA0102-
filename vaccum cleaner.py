import random
room = [[random.randint(0,1) for _ in range(2)] for _ in range(2)]

print("Initial Room:")
for r in room: print(r)

for i in range(2):
    for j in range(2):
        if room[i][j] == 1:
            print(f"Vacuum at ({i},{j}) -> Dirty, cleaning...")
            room[i][j] = 0
        else:
            print(f"Vacuum at ({i},{j}) -> Clean")
for r in room: print(r)
print("All cells cleaned!")
