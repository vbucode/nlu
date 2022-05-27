from words import Words
from nerclassifier import NerClassificator
import corpus

with open("data.txt", "r") as file:
    f = file.read()

# tokenize string to words
w = Words(f)
wl = w.load()
#print("\nworld tokenize:\n", wl)

# load ner
ner = corpus.ner()

# ner classification
ninst = NerClassificator(*ner)
n = ninst.load(wl)
print("\nner classification:\n", n)
