import unittest
import lambda_function

class MyTestCase(unittest.TestCase):
    def test_something(self):
        lambda_function.hello()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
