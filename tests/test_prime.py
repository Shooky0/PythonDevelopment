import unittest

from PrimeFinder.primetogether import is_prime


class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime_for_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))

    def test_is_prime_for_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    def test_is_prime_for_large_numbers(self):
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))


if __name__ == "__main__":
    unittest.main()
