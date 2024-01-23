# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_matches):
        word_sorted=sorted(self.word)
        return [anagram for anagram in possible_matches if sorted(anagram.lower())==word_sorted]
 
 