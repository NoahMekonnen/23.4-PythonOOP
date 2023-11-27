from wordfinder import WordFinder
from random import  choice


class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        self.list_of_words = []
        words_file = open(path, 'r')
        for ele in words_file:
            if ele[0] != " " and ele[0] != "#":
                self.list_of_words.append(ele[:len(ele)-1])
        print(f"{len(self.list_of_words)} words read")
    def random(self):
        return choice(self.list_of_words)

    
