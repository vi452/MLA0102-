# Backward Chaining Example

knowledge_base = {
    "mammal(A)": ["vertebrate(A)"],
    "vertebrate(A)": ["animal(A)"],
    "vertebrate(A),flying(A)": ["bird(A)"],
    "vertebrate('duck')": [],
    "flying('duck')": [],
    "mammal('cat')": []
}

def backward_chaining(goal):
    for rule, conclusions in knowledge_base.items():
        for c in conclusions:
            if c == goal:
                print(f"{goal} derived from {rule}")
                return True
    if goal in knowledge_base:
        print(f"{goal} is a known fact")
        return True
    return False

# Test queries
backward_chaining("bird(A)")
backward_chaining("animal(A)")
backward_chaining("mammal('cat')")
