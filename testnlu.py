from words import Words
from nerclassifier import NerClassificator

with open("data.txt", "r") as file:
    f = file.read()

# tokenize to words
w = Words(f)
wl = w.load()
#print("\nword tokenize:\n", wl)

# ner classification
ner = NerClassificator(wl)
n = ner.load()
print("\nner classification:\n", n)
