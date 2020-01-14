"""File that holds fraction class."""


class Fraction:
    """Class for Fractions in Python."""

    def __init__(self, numerator=1, denominator=1):
        """Defailt constructor for Fraction."""
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        """Str Representation of fraction."""
        return self.numerator + "/" + self.denominator

    def __str__(self):
        """Str representation of fraction."""
        return self.numerator + "/" + self.denominator

    @classmethod
    def from_int(cls, number):
        """Take a int and return a fraction."""
        return Fraction(number, 1)
