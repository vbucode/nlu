from words import Words

nerlist = []
triallist = []
llist = []
rlist = []
var = 0

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
        global var
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
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
                                triallist.append([k, rlist[llist.index(j)].replace("\n", "")])
                            if len(triallist) == len(wl):
                                for n in triallist:
                                    if triallist.index(n) == 0:
                                        nerlist.append((n[0], "b-" + n[1]))
                                    elif triallist.index(n) == len(triallist) - 1:
                                        nerlist.append((n[0], "i-" + n[1]))
                                    elif triallist.index(n) != 0 and triallist.index(n) != -1:
                                        nerlist.append((n[0], n[1]))
                                var = len(wl) - 1
                        break
                    elif count == len(llist):
                        nerlist.append((i, "out"))
        return nerlist
