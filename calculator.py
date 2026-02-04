def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


print("\nHello! Welcome to thecalculator! What would you like to do today?\n")
print("1. Addition")
print("2. Subtraction\n")
print("3. Multiplication")
print("4. division")

operation = int(input("Type your option (1-4): "))
n1 = int(input("Type your first number: "))
n2 = int(input("Type your second number: "))

if operation == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif operation == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif operation == 3:
    print(n1, "*", n2, "=", multi(n1, n2))
elif operation == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")