# Monkey and Banana Proble
def monkey_banana():
    monkey = "floor"
    box = "corner"
    banana = "ceiling"
    has_banana = False
    print("Initial State: Monkey on floor, Box in corner, Banana hanging from ceiling"
    box = "under banana"
    print("Monkey moves box under the banana")
    monkey = "on box"
    print("Monkey climbs onto the box")
    if monkey == "on box" and box == "under banana":
        has_banana = True
        banana = "with monkey"
        print("Monkey grabs the banana!")
    if has_banana:
        print("Goal achieved: Monkey has the banana!")
    else:
        print("Goal not achieved!")
monkey_banana()


output:
Initial State: Monkey on floor, Box in corner, Banana hanging from ceiling
Monkey moves box under the banana
Monkey climbs onto the box
Monkey grabs the banana!
Goal achieved: Monkey has the banana!

