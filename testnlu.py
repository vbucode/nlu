from words import Words
from nerclassifier import NerClassifier
import corpus


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

# load stop words
stop = corpus.stopwords("russian")
for i in wl:
        stopfiltered = [str(x) for x in wl if x not in stop]
print("\nwithout stop words:\n", stopfiltered)

# ner classification
ner = NerClassifier(stopfiltered)
n = ner.load()
print("\nner classification:\n", n)

# classification
clas = Classirier(stopfiltered)
s = clas.load()
print("\nclassification:\n", s)
