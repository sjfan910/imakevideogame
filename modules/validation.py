import os
import urllib.request

'''
ok, we need to create a file where we allow the game to build a trie. For this we need 2 classes:

TrieNode, where its the individual nodes in the trie. A children is a dictionary mapping letter to the next node such as {'A': TrieNode, 'P': TrieNode}. is_word is if the path leading to this node spells a complete valid word. 

Trie: This is the actual prefix tree. it needs the following:

 - insert(word) - we load every dictionary word into the trie at startup.
 - search(word) - checks if a full word exists when a player submits a word
 - starts_with (prefix) - this is pruning. it checks if any word starts with the current sequece of letters

WordValidator: 

 - load_dictionary(path) - reads the dictionary and inserts every word above 3 letters into the trie. 
 - is_valid_word(word) - public interface for the game. 


Trie, where it contains 


'''


class TrieNode:
    #Each node can have up to 26 children and may represent the end of a word
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.meaning = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, meaning=None):
        current = self.root
        for char in word.upper():
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEndOfWord = True

        if meaning is not None:
            current.meaning = meaning

    def starts_with(self, prefix): 
        #Call this when dictrie is built
        node = self.root
        for char in prefix.upper():
            if char not in node.children:
                return False
            node = node.children[char] #traverses downwards
        return True
    
class WordValidator:
    difficulty_map = {'easy': 'data/easy.txt', 'medium': 'data/medium.txt', 'hard': 'data/hard.txt'}

    def __init__(self, difficulty):
        self.dictionary_path = self.difficulty_map.get(difficulty)
        self.trie = Trie()
    
    def download_dictionary():
        if not os.path.exists('data'):
            os.makedirs('data')
        
        url = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
        filepath = 'enable1.txt'

        if os.path.exists(filepath):
            return
        
        print("Downloading dictionary…")
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"Downloaded to {filepath}")

            with open(filepath, 'r') as f:
                word_count = sum(1 for line in )
    def load_dictionary(self, path):
        if not os.path.exists(path):
            user_download = input(f"Didn't find dictionary at {path}, should we download it now?")
            if user_download == 'yes':
                download_dictionary()
            return
        try:
            with open(path, 'r') as f:
                word_count = 0
                for line in f:
                    word = line.strip().upper()
                    