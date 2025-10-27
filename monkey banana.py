# Monkey and Banana Problem

def monkey_banana():
    monkey = "floor"
    box = "corner"
    banana = "ceiling"
    has_banana = False

    print("Initial State: Monkey on floor, Box in corner, Banana hanging from ceiling")

    # Step 1: Monkey moves the box under the banana
    box = "under banana"
    print("Monkey moves box under the banana")

    # Step 2: Monkey climbs onto the box
    monkey = "on box"
    print("Monkey climbs onto the box")

    # Step 3: Monkey takes the banana
    if monkey == "on box" and box == "under banana":
        has_banana = True
        banana = "with monkey"
        print("Monkey grabs the banana!")

    # Final state
    if has_banana:
        print("Goal achieved: Monkey has the banana!")
    else:
        print("Goal not achieved!")

# Run the program
monkey_banana()

####3
