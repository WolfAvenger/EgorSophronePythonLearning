import unittest
import Task_2
import time

class Test_test_2(unittest.TestCase):

    def test_even(self):
        n = 8

        result = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0]
        ]

        self.assertListEqual(Task_2.ChessPlate(n), result, msg="Test 1 not passed")

    def test_odd(self):
        n = 7
        result = [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0]
        ]

        self.assertListEqual(Task_2.ChessPlate(n), result, msg="Test 2 not passed")


    def test_stress(self):
        n = 250
        result = []
        with open('big_chess.txt') as file:
            for line in file:
                result.append(list(map(int, line.split())))

        clock = time.time()
        work = Task_2.ChessPlate(n)
        clock = time.time() - clock

        self.assertListEqual(work, result, msg="Test 3 not passed")
        self.assertLessEqual(clock, 0.0001, msg = 'Reached time limit of 80 microseconds')


if __name__ == '__main__':
    unittest.main()
