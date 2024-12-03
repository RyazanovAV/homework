from  pprint import pprint
import os

class WordsFinder:
    def __init__(self, *files_name):
        self.files_name = files_name

    def get_all_words(self):
        all_words = {}
        replace_val = {',': '', '.': '', '=': '', '!': '', '?': '', ';': '', '.': '', ' - ': '', '\n': ' ', ':': ''}
        for f in self.files_name:
            with open(f, encoding='utf-8') as file:
                st = file.read()
            for i, j in replace_val.items():
                st = st.replace(i, j)
            all_words[f] = st.lower().split()
        return all_words
    def find(self, word):
        pos_word = {}
        for it, val in self.get_all_words().items():
            if word in val:
                vl = val.index(word)+1
            else:
                vl = 'нет элемента в списке'
            pos_word[it] = vl
        return pos_word
    def count(self, word):
        pos_word = {}
        for it, val in self.get_all_words().items():
            pos_word[it] = val.count(word)
        return pos_word

m = WordsFinder('df.txt', 'tes1.txt')
for i, k in m.get_all_words().items():
    print(i, k)

print(m.find("a"))
print(m.count('text'))
