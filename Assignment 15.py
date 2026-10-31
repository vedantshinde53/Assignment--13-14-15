import gc

class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "object destroyed")

# Create objects
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

# Delete objects
del obj1
del obj2

print("Garbage collection started")

# Manual garbage collection
collected = gc.collect()

print("Garbage collected:", collected)