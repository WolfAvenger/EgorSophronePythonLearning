import unittest
import Task_3

class Test_test_1(unittest.TestCase):
    def test_d4(self):
        inp = 'd4'
        result = []
        with open('test_d4.txt') as file:
            for line in file:
                result.append(list(map(str, line.split())))
        self.assertListEqual(Task_3.HorseTurns(inp), result, msg = "Test 1 not passed")

    def test_a1(self):
        inp = 'a1'
        result = []
        with open('test_a1.txt') as file:
            for line in file:
                result.append(list(map(str, line.split())))
        self.assertListEqual(Task_3.HorseTurns(inp), result, msg = "Test 2 not passed")

    def test_b7(self):
        inp = 'b7'
        result = []
        with open('test_b7.txt') as file:
            for line in file:
                result.append(list(map(str, line.split())))
        self.assertListEqual(Task_3.HorseTurns(inp), result, msg = "Test 3 not passed")
        

if __name__ == '__main__':
    unittest.main()
