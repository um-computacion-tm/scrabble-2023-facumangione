lectern_size = 7

class Player:
    def __init__(self, name = "", number = 0, points = 0, bag_tiles = None):
        self.points = points
        self.name = name
        self.number = number 
        self.lectern = [] 

    def give_tiles(self, tiles = []):
        self.lectern.extend(tiles)

    def fill(self, bag_tiles):
        size = len(self.lectern) 
        self.give_tiles(bag_tiles.take(7 - size))
        
    def change_tiles(self, old_tiles_index = [], new_tiles = []):
        old_tiles = []
        for i in range(len(old_tiles_index)):
            old_tiles.append(self.lectern[old_tiles_index [i]-1])
            self.lectern[old_tiles_index [i]-1] = new_tiles[i]
        return old_tiles
    
    def split_word(self,word):
        word = word.upper()
        if 'CH' in word:
            word = word.replace('CH','1')
        elif 'LL' in word:
            word =word.replace('LL','2')
        elif 'RR' in word:
            word = word.replace('RR', '3')
        result_word = []
        for letter in word:
            if letter == '1':
                result_word.append('CH')
            elif letter == '2':
                result_word.append('LL')
            elif letter == '3':
                result_word.append('RR')
            else:
                result_word.append(letter)
        return result_word

    def search_words_in_lectern(self, word):
        word = self.split_word(word)
        lectern = self.lectern
        valid = 0
        for letter in word:
            for tile in lectern:
                if letter == tile.letter:
                    valid += 1
                    lectern.remove(tile)
                    break
        if valid == len(word):
            return True
        return False  
    
    def take_tiles(self,word):
        word = self.split_word(word)
        tiles=[]
        for letter in word:
            for tile in self.lectern:
                if tile == letter.upper():
                    tiles.append(tile)
                    self.lectern.remove(tile)
                    break
        return tiles

    def view_lectern(self):
        lectern = '                     ATRIL\n\nLetras ->  |'
        for tile in self.lectern:
            lectern += f' {tile} |'
        return lectern
    
    def has_tiles(self,word):
        word = self.split_word(word)
        for letter in word:
            if letter.upper() not in self.view_lectern():
                return False
        return True