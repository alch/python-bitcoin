from bc.point import Point
from bc.s256_field import S256Field
from bc.signature import Signature

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Point(Point):
    """
    Point in the secp256k1 curve.

    See See https://en.bitcoin.it/wiki/Secp256k1

    'a' and 'b' are defined as constants. Note that constructor arguments
    a,b here are unused, but they are required becuse the parent Point
    class uses the idiom
    <code>self.__class__(x, y, self.a, self.b)</code> to return new instances
    of the invoking class.
    """

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

    def verify(self, z, sig: Signature):
        s_inv = pow(sig.s, N - 2, N)
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u * G + v * self

        return total.x.num == sig.r


# Base point in secp256k1 curve.
G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
)
