from bc.field_element import FieldElement

P = 2 ** 256 - 2 ** 32 - 977


class S256Field(FieldElement):
    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)
