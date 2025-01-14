class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n

    def cube(self):
        return self.n * self.n * self.n

    def root(self):
        return self.n ** 0.5

# Main program
n = int(input("Enter a number: "))
action = input("Enter the action you want to perform (square, cube, root): ").lower()

# Create the Calculator object
calculator = Calculator(n)

# Perform the selected action
match action:
    case "square":
        print(f"The square of {n} is: {calculator.square()}")
    case "cube":
        print(f"The cube of {n} is: {calculator.cube()}")
    case "root":
        print(f"The square root of {n} is: {calculator.root()}")
    case _:
        print("Invalid action. Please choose from 'square', 'cube', or 'root'.")


