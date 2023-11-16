import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

# 테스트 코드
class TestAdd(unittest.TestCase):
    def test_add(self):
        print('더하기 테스트')
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        print('빼기 테스트')
        self.assertEqual(sub(7, 2), 5)

    def test_mul(self):
        print('곱하기 테스트')
        self.assertEqual(mul(1, 3), 3)

    def test_LEE(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()