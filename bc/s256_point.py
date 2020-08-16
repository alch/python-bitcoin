from bc.point import Point
from bc.s256_field import S256Field

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(S256Field(x), S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return 'S256Point({}, {})'.format(self.x, self.y)

    def __rmul__(self, coefficient):
        """
        We can define __rmul__ more efficiently because we know the order 'n' of 
        the group in secp256kl. We can mod by 'n' because nG = 0 (every 'n' times
        we cycle back to zero)
        """
        coef = coefficient % N
        return super().__rmul__(coef)