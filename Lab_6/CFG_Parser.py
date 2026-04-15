import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> VP
VP -> V NP NP
V -> 'يكتب'
NP -> 'الولد' | 'الواجب'
""")

parser = nltk.ChartParser(grammar)

sentence = ['يكتب', 'الولد', 'الواجب']

for tree in parser.parse(sentence):
    print(tree)