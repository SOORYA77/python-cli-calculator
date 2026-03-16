def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    print("Simple CLI Calculator")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    op = input("Choose operation (+ - * /): ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()
