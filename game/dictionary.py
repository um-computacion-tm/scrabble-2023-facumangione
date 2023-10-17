import unicodedata

class Dictionary:

    with open('dictionary.txt', 'r', encoding='utf-8') as file:
        word_list = set(word.strip().lower() for word in file)

    def remove_accents(self,word):
        word = ''.join(x for x in unicodedata.normalize('NFKD', word) if not unicodedata.combining(x))
        return word
    def verify_word(self, word):
        return word.lower() in self.word_list