import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_remove_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.remove_accents(word), "Imaginacion")
    def test_simple_verify(self):
        dic = Dictionary()
        word = "Hola"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_false_word(self):
        dic = Dictionary()
        word = "Kadabra"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Pingüino"
        self.assertEqual(dic.verify_word(word), True)

if __name__ == '__main__':
    unittest.main()