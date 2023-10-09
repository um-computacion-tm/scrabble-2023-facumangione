import unittest

from game.dictionary import validate_word

class TestDictionary(unittest.TestCase): 

    def test_verificar_palabra_existente():
    # Prueba para una palabra que debería existir
        assert validate_word("perro") == True

    def test_verificar_palabra_inexistente():
    # Prueba para una palabra que no debería existir
        assert validate_word("xyzabc") == False

    def test_verificar_palabra_vacia():
    # Prueba para una palabra vacía
        assert validate_word("") == False



if __name__ == '__main__':
    unittest.main()