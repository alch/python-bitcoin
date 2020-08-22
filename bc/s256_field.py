from bc.field_element import FieldElement

# p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F
P = 2 ** 256 - 2 ** 32 - 977


class S256Field(FieldElement):
    """
    Field element for the the secp256k1 curve.

    See https://en.bitcoin.it/wiki/Secp256k1

    'p' is defined as constant. Note that the constructor arguments
    'prime' is unused, but required because the parent FieldElement
    class uses the idiom
    <code>self.__class__(num, self.prime)</code> to return new instances
    of the invoking class.
    """
    def __init__(self, num, prime=None):
        # noinspection PyCompatibility
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)
