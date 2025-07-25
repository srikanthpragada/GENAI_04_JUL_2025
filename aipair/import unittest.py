import unittest
from prime import isprime

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(isprime(2))
        self.assertTrue(isprime(3))
        self.assertTrue(isprime(5))
        self.assertTrue(isprime(7))
        self.assertTrue(isprime(11))
        self.assertTrue(isprime(13))
        self.assertTrue(isprime(17))
        self.assertTrue(isprime(19))
        self.assertTrue(isprime(23))
        self.assertTrue(isprime(29))

    def test_non_prime_numbers(self):
        self.assertFalse(isprime(0))
        self.assertFalse(isprime(1))
        self.assertFalse(isprime(4))
        self.assertFalse(isprime(6))
        self.assertFalse(isprime(8))
        self.assertFalse(isprime(9))
        self.assertFalse(isprime(10))
        self.assertFalse(isprime(12))
        self.assertFalse(isprime(15))
        self.assertFalse(isprime(20))

    def test_negative_numbers(self):
        self.assertFalse(isprime(-1))
        self.assertFalse(isprime(-2))
        self.assertFalse(isprime(-17))

    def test_large_prime(self):
        self.assertTrue(isprime(101))

    def test_large_non_prime(self):
        self.assertFalse(isprime(100))

if __name__ == "__main__":
    unittest.main()