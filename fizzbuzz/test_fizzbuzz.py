from fizzbuzz import robot
import unittest

# define uma classe própria de testes, que herda de unittest.TestCase
class FizzBuzzTest(unittest.TestCase):
    # define os testes a serem executados (cenário de testes)
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_fizz_when_4(self):
        self.assertEqual(robot(4),'4')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3),'fizz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6),'fizz')

    def test_say_fizz_when_12(self):
        self.assertEqual(robot(12),'fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5),'buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10),'buzz')

    def test_say__when_20(self):
        self.assertEqual(robot(20),'buzz')

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15),'fizzbuzz')

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(robot(30),'fizzbuzz')


if __name__ == '__main__':
     unittest.main()
