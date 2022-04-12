from words import Words
from nerclassifier import NerClassificator

xlist = []

# to awoid some problems with not good writting text
# для избежания возможной ошибки при неправильном форматировании данных
with open("data.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row)
        varstring = " ".join(xlist)

# tokenize string to words
w = Words(varstring)
wl = w.load()
print("\nworld tokenize:\n", wl)

# ner classification
ner = NerClassificator(wl)
n = ner.load()
print("\nner classification:\n", n)
