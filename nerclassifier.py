import re

nerlist = []
llist = []
rlist = []

with open("ner-ru.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right.replace("\n", ""))

month = ["январь", "января", "октябрь", "октября", "года"]

class NerClassificator:
    def __init__(self, text):
        self.text = text
    def load(self):
        var = 0
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
                if i.isnumeric() and int(i):
                    flag = 0
                    for k in month:
                        if k == self.text[self.text.index(i) + 1]:
                            nerlist.append((i, "date"))
                            flag = 1
                    if flag == 0:
                        nerlist.append((i, "out"))
                elif i.isnumeric() == False:
                    for j in llist:
                        count += 1
                        clearlist = []
                        clearlist = re.split("[\-\s]", j)
                        if i == clearlist[0] and len(clearlist) == 1:
                            nerlist.append((i, rlist[llist.index(j)]))
                            break
                        elif i == clearlist[0] and len(clearlist) > 1:
                            count2 = 0
                            triallist = []
                            for k in clearlist:
                                count2 += 1
                                if k == self.text[self.text.index(i) + count2 - 1]:
                                    triallist.append([k, rlist[llist.index(j)]])
                            if len(triallist) == len(clearlist):
                                for n in triallist:
                                    if triallist.index(n) == 0:
                                        nerlist.append((n[0], "b-" + n[1]))
                                    elif triallist.index(n) == len(triallist) - 1:
                                        nerlist.append((n[0], "i-" + n[1]))
                                    elif triallist.index(n) != 0 and triallist.index(n) != -1:
                                        nerlist.append((n[0], n[1]))
                                var = len(clearlist) - 1
                            else:
                                nerlist.append((i, rlist[llist.index(j)]))
                                break
                        elif count == len(llist):
                             nerlist.append((i, "out"))
        return nerlist
