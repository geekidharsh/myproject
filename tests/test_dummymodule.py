import unittest
from mypackage import dummymodule

class TestDummyPackage(unittest.TestCase):

    def test_add(self):
        # Test the addition method
        dummy = dummymodule.DummyPack(10, 5)
        result = dummy.add()
        self.assertEqual(result, 15)

    def test_subtract(self):
        # Test the subtr method
        dummy = dummymodule.DummyPack(10, 5)
        result = dummy.subtract()
        self.assertEqual(result, 5)
