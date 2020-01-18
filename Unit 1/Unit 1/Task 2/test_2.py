import unittest
import Task_2

class Test_test_1(unittest.TestCase):
    def test_A(self):
        array = [1,2,3,4,5,6,7,8,9,10,11]
        result = [10,8,6,4,2]
        
        self.assertListEqual(Task_2.EachSecondReverse(array), result, "Test 1 not passed")

    def test_B(self):
        array = ['a', 'ab', 'abc', 13.2, False, 'yarn', 0, 33]
        result = [0, False, 'abc','a']

        self.assertListEqual(Task_2.EachSecondReverse(array), result, "Test 2 not passed")

    def test_ultimate(self):

        array = ['a', 'ab', 'abc', 13.2, False, 'yarn', 0, 33]
        if type(Task_2.SecondSolution(array)) == bool: self.fail(msg = "Решение не представлено")
        result = [0, False, 'abc','a']

        self.assertListEqual(Task_2.SecondSolution(array), result, "Test ULTIMATE not passed")

if __name__ == '__main__':
    unittest.main()
