from collatz import proximo, termos, maior_sequencia
import unittest

class ProximoTest(unittest.TestCase):
    def test_say_1_when_2(self):
        self.assertEqual(proximo(2), 1)

    def test_say_10_when_3(self):
        self.assertEqual(proximo(3), 10)

    def test_say_5_when_10(self):
        self.assertEqual(proximo(10), 5)



class TermosTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(termos(1), 1)

    def test_say_2_when_2(self):
        self.assertEqual(termos(2), 2)

    def test_say_5_when_16(self):
        self.assertEqual(termos(16), 5)

    def test_say_10_when_13(self):
        self.assertEqual(termos(13), 10)



class MaiorSequenciaTest(unittest.TestCase):

    def test_say_1_when_1(self):
        self.assertEqual(maior_sequencia(1), 1)

    def test_say_2_when_2(self):
        self.assertEqual(maior_sequencia(2), 2)

    def test_say_8_when_3(self):
        self.assertEqual(maior_sequencia(3), 3)

    def test_say_8_when_4(self):
        self.assertEqual(maior_sequencia(4), 3)

    def test_say_8_when_5(self):
        self.assertEqual(maior_sequencia(5), 3)

    def test_say_8_when_6(self):
        self.assertEqual(maior_sequencia(6), 6)

    def test_say_14_when_7(self): # 7 22 11 34 17 52 26 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        self.assertEqual(maior_sequencia(7), 7)

    def test_say_112_when_27(self):
        self.assertEqual(maior_sequencia(27), 27)

    def test_say_179_when_1000(self):
        self.assertEqual(maior_sequencia(1000), 871)

    def test_say_837_799_when_1_000_000(self):
        self.assertEqual(maior_sequencia(1000000), 837799)



if __name__ == '__main__':
     unittest.main()
