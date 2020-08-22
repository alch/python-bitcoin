import unittest
from random import randint
from bc.s256_point import N
from bc.private_key import PrivateKey


class TestPrivateKey(unittest.TestCase):
    def test_sign(self):
        pk = PrivateKey(randint(0, N))
        z = randint(0, 2**256)
        sig = pk.sign(z)
        self.assertTrue(pk.point.verify(z, sig))


if __name__ == "__main__":
    unittest.main()
