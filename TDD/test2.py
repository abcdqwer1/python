import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        print('곱하기 테스트')
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        print('곱하기 테스트')
        self.assertEqual(5, 5)

    def test_mul(self):
        print('곱하기 테스트')
        self.assertEqual(3, 3)

    def test_LEE(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()