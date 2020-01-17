import unittest
import Task_1
import math

class Test_test_1(unittest.TestCase):
    def test_A(self):
        array = [False, 13, 'abc', [1,3], 3.4, 81, 'shit', 0, 'set', True]
        result = [False, 3.4, True]

        self.assertListEqual(Task_1.boolOrFloat(array), result, "Test 1 not passed")

    def test_B(self):
        array = [0, 123, '123', math.e, False, {}, (1,2), True, 13.456, 1.1]
        result = [math.e, False, True, 13.456, 1.1]

        self.assertListEqual(Task_1.boolOrFloat(array), result, "Test 2 not passed")

if __name__ == '__main__':
    unittest.main()
