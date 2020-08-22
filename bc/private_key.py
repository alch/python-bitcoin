from hashlib import sha256
import hmac
from bc.s256_point import S256Point, N, G
from bc.signature import Signature


class PrivateKey:

    point: S256Point

    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)

    def sign(self, z):
        """
        Signs a message hash

        @param z: the duble-sha256-hashed message
        @return: Signature(r, s)
        """
        k = self.deterministic_k(z)
        r = (k * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N / 2:
            # Using the low-s value will get nodes to relay our transactions.
            s = N - s

        return Signature(r, s)

    def deterministic_k(self, z):
        """
        The
        PlayStation 3 hack back in 2010 was due to the reuse of the k value
        in multiple signatures. To combat this, there is a deterministic
        k generation standard that uses the secret and z to create a unique,
        deterministic k every time. The specification is in RFC 6979.

        @param z: the hashed message
        @return: a cryptographically safe, deterministic random k
        """
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, sha256).digest()
        v = hmac.new(k, v, sha256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, sha256).digest()
        v = hmac.new(k, v, sha256).digest()
        while True:
            v = hmac.new(k, v, sha256).digest()
            candidate = int.from_bytes(v, 'big')
            if 1 <= candidate < N:
                return candidate
            k = hmac.new(k, v + b'\x00', sha256).digest()
            v = hmac.new(k, v, sha256)