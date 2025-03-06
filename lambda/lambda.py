def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum is: {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
