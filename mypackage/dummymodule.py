class DummyPack:
    """
    This is a dummy package to try out distribution of a python package.
    This class initializes an object with two numbers and can perform various arithmetic on them"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Add the two numbers."""
        return self.num1 + self.num2

    def subtract(self):
        """Subtract num2 from num1."""
        return self.num1 - self.num2

    def multiply(self):
        """Multiply the two numbers."""
        return self.num1 * self.num2

    def divide(self):
        """Divide num1 by num2."""
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed."