import unittest
import Task_3

class Test_test_1(unittest.TestCase):
    def test_A(self):
        array1 = [4,2,3.3,7]
        array2 = [0, 19.8 ,33, 4]

        result = {2:0, 3.3:4, 4:19.8, 7:33}

        self.assertDictEqual(Task_3.ArraysPairing(array1, array2), result, "Test 1 not passed")

    def test_B(self):
        array1 = [5,9,10,-3]
        array2 = [0, 19 ,33, 0]

        result = {-3:0, 5:0, 9:19, 10:33}

        self.assertDictEqual(Task_3.ArraysPairing(array1, array2), result, "Test 1 not passed")

if __name__ == '__main__':
    unittest.main()
