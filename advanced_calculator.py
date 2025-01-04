import re
import math

class AdvanceCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0.0  # For memory operations

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(n)

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def sine(self, x):
        return math.sin(math.radians(x))

    def cosine(self, x):
        return math.cos(math.radians(x))

    def tangent(self, x):
        return math.tan(math.radians(x))

    def logarithm(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive values.")
        return math.log(x, base)

    def natural_logarithm(self, x):
        if x <= 0:
            raise ValueError("Natural logarithm is not defined for non-positive values.")
        return math.log(x)

    def exponential(self, x):
        return math.exp(x)

    def store_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0.0

    def parse_input(self, input_string):
        pattern = r"^(\d+\.?\d*)\s*([+\-*/^])\s*(\d+\.?\d*)$"
        match = re.match(pattern, input_string)
        if match:
            num1, operator, num2 = match.groups()
            return float(num1), operator, float(num2)
        raise ValueError("Invalid input format.")

    def evaluate_expression(self, expression):
        try:
            num1, operator, num2 = self.parse_input(expression)
            if operator == '+':
                result = self.add(num1, num2)
            elif operator == '-':
                result = self.subtract(num1, num2)
            elif operator == '*':
                result = self.multiply(num1, num2)
            elif operator == '/':
                result = self.divide(num1, num2)
            elif operator == '^':
                result = self.power(num1, num2)
            else:
                raise ValueError("Unknown operator.")
            self.history.append((expression, result))
            return result
        except ValueError as e:
            return str(e)

    def undo_last_operation(self):
        if self.history:
            self.history.pop()
            return "Last operation undone."
        return "No operations to undo."

    def show_history(self):
     if not self.history:
        return "No history available."
     return "\n".join(
        f"{expr} = {int(result) if result.is_integer() else result}"
        for expr, result in self.history
    )

# Example usage
if __name__ == "__main__":
    calculator = AdvanceCalculator()

    while True:
        print("\nAdvanced Scientific Calculator")
        print("1. Basic Operations (+, -, *, /, ^)")
        print("2. Factorial")
        print("3. Prime Check")
        print("4. Trigonometric Functions (sin, cos, tan)")
        print("5. Logarithms (log10, natural log)")
        print("6. Exponential")
        print("7. Memory Operations (Store, Recall, Clear)")
        print("8. Undo Last Operation")
        print("9. Show History")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            expression = input("Enter expression (e.g., 5 + 3): ")
            print("Result:", calculator.evaluate_expression(expression))

        elif choice == '2':
            number = int(input("Enter a number: "))
            try:
                print("Factorial:", calculator.factorial(number))
            except ValueError as e:
                print(e)

        elif choice == '3':
            number = int(input("Enter a number: "))
            print("Is Prime:", calculator.is_prime(number))

        elif choice == '4':
            func = input("Enter function (sin, cos, tan): ").strip().lower()
            angle = float(input("Enter angle in degrees: "))
            if func == 'sin':
                print("Sine:", calculator.sine(angle))
            elif func == 'cos':
                print("Cosine:", calculator.cosine(angle))
            elif func == 'tan':
                print("Tangent:", calculator.tangent(angle))
            else:
                print("Invalid function.")

        elif choice == '5':
            log_type = input("Enter log type (log10, ln): ").strip().lower()
            number = float(input("Enter number: "))
            try:
                if log_type == 'log10':
                    print("Logarithm (base 10):", calculator.logarithm(number))
                elif log_type == 'ln':
                    print("Natural Logarithm:", calculator.natural_logarithm(number))
                else:
                    print("Invalid log type.")
            except ValueError as e:
                print(e)

        elif choice == '6':
            number = float(input("Enter number: "))
            print("Exponential (e^x):", calculator.exponential(number))

        elif choice == '7':
            mem_op = input("Enter memory operation (store, recall, clear): ").strip().lower()
            if mem_op == 'store':
                value = float(input("Enter value to store: "))
                calculator.store_memory(value)
                print("Value stored in memory.")
            elif mem_op == 'recall':
                print("Recalled value:", calculator.recall_memory())
            elif mem_op == 'clear':
                calculator.clear_memory()
                print("Memory cleared.")
            else:
                print("Invalid memory operation.")

        elif choice == '8':
            print(calculator.undo_last_operation())

        elif choice == '9':
            print(calculator.show_history())

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.") 
