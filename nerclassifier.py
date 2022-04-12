#class NER Classification
from words import Words

nerlist = []
triallist = []
llist = []
rlist = []

with open("nerru.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)
class NerClassificator:
    def __init__(self, text):
        self.text = text
    def load(self):
        count4 = 0
        for i in self.text:
            count = 0
            print(i)
            while count4 - 1 > 0:
                count4 -= 1
            for j in llist:
                count += 1
                w = Words(j)
                wl = w.load()
                if wl[0] == i and len(wl) == 1:
                    nerlist.append((i, rlist[llist.index(j)].replace("\n", "")))
                    break
                elif wl[0] == i and len(wl) > 1:
                    count2 = 0
                    for k in wl:
                        count2 += 1
                        if k == self.text[self.text.index(i) + count2 - 1]:
                            triallist.append((k, rlist[llist.index(j)].replace("\n", "")))
                    if len(triallist) == len(wl):
                        count3 = 0
                        for n in triallist:
                            count3 += 1
                            if n[0]:
                                nerlist.append((n[0][0], "b-" + n[0][1]))
                            elif n[-1]:
                                nerlist.append((n[-1][0], "i-" + n[-1][1]))
                            else:
                               nerlist.append((n[count2 - 1][0], n[count3 - 1][1]))
                            count4 = len(wl)
                    break
                if count == len(llist):
                    nerlist.append((i, "out"))
        return nerlist
