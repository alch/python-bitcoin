from __future__ import annotations

class FieldElement:
    def __init__(self, num: int, prime: int):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
 
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)
 
    def __eq__(self, other: int) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: int) -> bool:
        return not self == other

    def __add__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __truediv__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        num = pow(self.num * other.num, self.prime - 2) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> FieldElement:
        num = pow(self.num, exponent, self.prime)
        return self.__class__(num, self.prime)


if __name__ == "__main__":
    a = FieldElement(95, 97)
    b = FieldElement(45, 97)
    c = FieldElement(31, 97)

    print(a * b * c)

    a = FieldElement(17, 97)
    b = FieldElement(13, 97)
    c = FieldElement(19, 97)
    d = FieldElement(44, 97)

    print(a * b * c * d)

    a = FieldElement(12, 97)
    b = FieldElement(77, 97)

    print(a**7 * b**49)

    ps = [7, 11, 17, 31]
    for p in ps:
        e = []
        for f in range(1, p-1):
            e.append(pow(FieldElement(f, p), (p-1)))
        print(e)
