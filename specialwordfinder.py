from wordfinder import WordFinder
from random import  choice


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        
    def make_list(self):
        words_file = open(self.path, 'r')
        for ele in words_file:
            if ele[0] != " " and ele[0] != "#":
                self.list_of_words.append(ele[:len(ele)-1])

    def random(self):
        return choice(self.list_of_words)

    
