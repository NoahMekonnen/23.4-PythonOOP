"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    235886 words read
    """
    def  __init__(self,path):
        self.path = path
        self.list_of_words = []
        with open(self.path, 'r') as file:
            for line in file:
                new_line = line[:len(line)-1]
                self.list_of_words.append(new_line)
        print(f"{len(self.list_of_words)} words read")
        file.close()        

    def random(self):
        """return random word from the file"""
        return choice(self.list_of_words)

