from words import Words
from nerclassifier import NerClassificator

with open("data.txt", "r") as file:
    f = file.read()

# tokenize string to words
w = Words(f)
wl = w.load()
#print("\nworld tokenize:\n", wl)

# ner classification
ner = NerClassificator(wl)
n = ner.load()
print("\nner classification:\n", n)
