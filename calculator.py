def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

print("\nHello! Welcome to thecalculator! What would you like to do today?\n")
print("1. Addition")
print("2. Subtraction\n")

operation = int(input("Type your option (1-2): "))
n1 = int(input("Type your first number: "))
n2 = int(input("Type your second number: "))

if operation == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif operation == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
else:
    print("Invalid input")