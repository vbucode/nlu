#class NERClassification

nerlist = []
llist = []
rlist = []

with open("ner.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)
class NerClassifier:
    def __init__(self, text):
        self.text = text
    def load(self):
        for i in self.text:
            flag = 1
            for j in llist:
                if i == j:
                    nerlist.append((i, rlist[llist.index(j)].replace("\n", "")))
                    flag = 0
                    break
            if flag != 0:
                nerlist.append((i, "out"))
        return nerlist
