from __future__ import annotations


class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        # Coding point at infinity
        if x is None and y is None:
            return
        if y ** 2 != x ** 3 + a * x + b:
            raise ValueError("({}, {}) is not on the curve".format(x, y))

    def __eq__(self, other: Point) -> bool:
        return self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y

    def __add__(self, other: Point) -> Point:
        if self.a != other.a and self.b != other.b:
            raise ValueError("Points ({}, {}) are not on the same curve".format(self, other))

        # self.x being "None" means that self is the point at infinity, 
        # or the additive identity. Thus, we return other.
        if self.x is None:
            return other

        # other.x being "None" means that other is the point at infinity, 
        # or the additive identity. Thus, we return self.
        if other.x is None:
            return self

        # When two points are additive inverses (that is, they have the same x but 
        # a different y, causing a vertical line) we should return the point at infinity.
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # Point Addition for When x1 != x2
        if self.x != other.x:
            # s is the slope of the line passing from P1 and P2
            s = (other.y - self.y) / (other.x - self.x)
            x3 = s ** 2 - self.x - other.x
            y3 = s * (self.x - x3) - self.y

        # Point addition when P1 == P2, meaning that the point
        # is tangent to the elliptical curve
        if self == other:

            if self.y == 0 * self.x:
                # We cannot simply compare y == 0 (scalar), since
                # if we are using finite fields instead of real numbers,
                # the 0 value must also be a finite field. Mutiplying 0
                # to an other finite field (like self.x) makes this zero
                # coparison work both in real and finite fields

                # Special case when the tangent is a vertical line,
                # with undefined slope. The addition will return the
                # Point at infinity
                return self.__class__(None, None, self.a, self.b)

            # s is the slope of the tangent point P1 == P2 in the curve
            s = (3 * (self.x ** 2) + self.a) / (2 * self.y)
            x3 = s ** 2 - 2 * self.x
            y3 = s * (self.x - x3) - self.y

        return self.__class__(x3, y3, self.a, self.b)

    def __rmul__(self, coefficient):
        """
        Multiplication with binary expansion that allows us
        to perform multiplications in log2(n) loops
        """
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result

    def __repr__(self):
        return "Point_{}_{}_({}, {})".format(self.x, self.y, self.a, self.b)
