import unittest
import Task_1
import time

class Test_test_1(unittest.TestCase):

    def test_A(self):
        array = [
            [0, 3, 2, 4],
            [2, 3, 1, 0],
            [5, 1, 2, 3],
            ]

        result = [2, 0]

        self.assertListEqual(Task_1.FirstMaximum(array), result, msg="Test 1 not passed")

    def test_repeated_values(self):
        array = [
            [0, 3, 2, 4],
            [2, 3, 5, 5],
            [5, 1, 2, 3],
            ]
        result = [1, 2]

        self.assertListEqual(Task_1.FirstMaximum(array), result, msg="Test 2 not passed")


    def test_negative_values(self):
        array = [
            [-5, -3, -2, -4],
            [-2, -3, -5, -5],
            [-5, -1, -2, -3],
            ]
        result = [2, 1]

        self.assertListEqual(Task_1.FirstMaximum(array), result, msg="Test 3 not passed")


    def test_giant_arrays(self):
        array=[]
        file=open('big_array.txt','r')
        for line in file:
            array.append(list(map(int,line.split())))
        result = [0, 112]

        clock = time.time()
        got = Task_1.FirstMaximum(array)
        clock=time.time() - clock
        file.close()

        self.assertListEqual(got, result, msg="Test 4 not passed due to wrong answer")
        self.assertLessEqual(clock, 0.064, msg="Test 4 not passed due to time limit (Program works more than 64 milliseconds)")


if __name__ == '__main__':
    unittest.main()
