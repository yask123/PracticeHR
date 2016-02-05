class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return str(num) + '/' + str(den)


a = Fraction(2, 3)

b = Fraction(3, 1)

print a + b
