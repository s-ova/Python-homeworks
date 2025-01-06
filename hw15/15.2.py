import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        if isinstance(a, float) or isinstance(b, float):
            a, b = self._convert_float_to_fraction(a, b)
        gcd = math.gcd(a, b)
        self.a = a // gcd
        self.b = b // gcd

    @staticmethod
    def _convert_float_to_fraction(a, b):
        """Converting a float to a proper fraction"""
        scale = 10 ** max(len(str(a).split(".")[1]), len(str(b).split(".")[1]))
        a, b = int(a * scale), int(b * scale)
        return a, b

    def __add__(self, other):
        numerator = self.a * other.b + self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.a * other.b - self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6', 'Test failed for addition'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3', 'Test failed for multiplication'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', 'Test failed for subtraction'

assert f_d < f_c, 'Test failed for less than comparison'
assert f_d > f_e, 'Test failed for greater than comparison'
assert f_a != f_b, 'Test failed for inequality'

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2, 'Test failed for equality with normalization'

f_float = Fraction(0.5, 0.75)
assert str(f_float) == 'Fraction: 2, 3', 'Test failed for float handling'

print('OK')