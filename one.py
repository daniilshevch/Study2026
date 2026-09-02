print("one line")
print("Added on new branch")
print("One more line")

for i in range(5):
    print(i)

def add(a, b):
    print(f"{a} + {b} = {a + b}")
def perform_operation(a, b, operation):
    if operation == "add":
        add(a, b)
    else:
        print("Operation not supported")

perform_operation(3, 4, "add")

def minus(a, b):
    print(f"{a} - {b} = {a - b}")

perform_operation(10, 5, "minus")

for p in range(3):
    print(f"Loop iteration: {p}")

