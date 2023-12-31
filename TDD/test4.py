import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        print(dir(self))
        self.assertEqual(add(1, 2), 3) # 같은지 판별
        self.assertTrue(10 == 10) # True인지 
        self.assertFalse(1 == 10) # False인지
        self.assertGreater(10, 1) # 앞에 것이 뒤에것보다 큰지
        self.assertLess(1, 10)    # 앞에 것이 뒤에것보다 작은지
        self.assertIn(1, [1, 2, 3, 4, 5]) # 포함하고 있는지
        self.assertIsInstance('a', str) # 인스턴스인지
        self.assertIn(1, [2, 3, 1])

if __name__ == '__main__':
    unittest.main()

