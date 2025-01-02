import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        side = math.ceil(total_area**0.5)
        while total_area % side != 0:
            side -= 1
        height = total_area // side
        return Rectangle(side, height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)) or n <= 0:
            raise ValueError("Multiplier must be a positive number.")
        total_area = self.get_square() * n
        side = math.ceil(total_area**0.5)
        while total_area % side != 0:
            side -= 1
        height = total_area // side
        return Rectangle(side, height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
print(r3)  # Rectangle(width=13, height=2)

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)  # Rectangle(width=8, height=4)

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print('All tests have been passed successfully')