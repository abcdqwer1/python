from django.test import TestCase

class Test(TestCase):

    def test_something_a(self):
        print('main a[[test]]')
        self.assertEqual(True, True)

    def test_something_b(self):
        print('main b[[test]]')
        self.assertEqual(True, True)
