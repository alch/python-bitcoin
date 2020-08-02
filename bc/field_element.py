from __future__ import annotations


class FieldElement:
    def __init__(self, num: int, prime: int):
        if num >= prime or num < 0:
            error = "Num {} not in field range 0 to {}".format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other: int) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: int) -> bool:
        return not self == other

    def __add__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different Fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different Fields")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different Fields")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __truediv__(self, other: FieldElement) -> FieldElement:
        '''
        See Fermat's little theorem for the theory behind the
        finite field division: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem

        Also note that modulo is not the reminder! See https://bit.ly/30lNfGE
        '''
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")
        num = pow(self.num * other.num, self.prime - 2) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> FieldElement:
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)

