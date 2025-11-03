# Program: Ontology Parsing using Triples
# Question 30 – AI & Expert System (MLA0102)

# ---- Knowledge Graph Structure ----
knowledge_graph = {}


# Insert triple ("Subclass", "Superclass")
def add_triple(subclass, superclass):
    if superclass not in knowledge_graph:
        knowledge_graph[superclass] = []
    knowledge_graph[superclass].append(subclass)


# Get all subclasses of given class
def get_subclasses(class_name):
    if class_name not in knowledge_graph:
        return []
    return knowledge_graph[class_name]


# Recursive function to check subclass relationship
def is_subclass(child, parent):
    if parent not in knowledge_graph:
        return False
    if child in knowledge_graph[parent]:
        return True
    return any(is_subclass(child, superclass) for superclass in knowledge_graph[parent])


# ---- Sample Ontology Triples (Input) ----
add_triple("Car", "Vehicle")
add_triple("Bike", "Vehicle")
add_triple("SportsCar", "Car")
add_triple("ElectricCar", "Car")
add_triple("Sedan", "Car")

# ---- Display Knowledge Graph ----
print("\nKnowledge Graph (Class → Subclasses):")
for parent, children in knowledge_graph.items():
    print(parent, "→", children)


# ---- Queries ----
search_class = "Car"
print("\nSubclasses of", search_class + ":", get_subclasses(search_class))

child = "SportsCar"
parent = "Vehicle"
print(f"\nIs '{child}' a subclass of '{parent}'? :", is_subclass(child, parent))
