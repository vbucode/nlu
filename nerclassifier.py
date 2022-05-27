import re

month = ["январь", "января", "февраль", "февраля", "март", "марта", "апрель", "апреля",
         "май", "мая", "июнь", "июня", "июль", "июля", "август", "августа",
         "сентябрь", "сентября", "октябрь", "октября", "ноябрь", "ноября", "декабрь", "декабря",
         "года", "году"]

class NerClassificator:
    def __init__(self, llist, rlist):
        self.llist = llist
        self.rlist = rlist
        self.nerlist = []
    def load(self, text):
        self.text = text 
        var = 0
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
                if i.isnumeric() == True:
                    flag = 0
                    for k in month:
                        if k == self.text[self.text.index(i) + 1]:
                            self.nerlist.append((i, "date"))
                            flag = 1
                    if flag == 0:
                        self.nerlist.append((i, "out"))
                elif i.isnumeric() == False:
                    for j in self.llist:
                        count += 1
                        clearlist = []
                        clearlist = re.split("[\-\s]", j)
                        if i == clearlist[0] and len(clearlist) == 1:
                            self.nerlist.append((i, self.rlist[self.llist.index(j)]))
                            break
                        elif i == clearlist[0] and len(clearlist) > 1:
                            count2 = 0
                            triallist = []
                            for k in clearlist:
                                count2 += 1
                                if k == self.text[self.text.index(i) + count2 - 1]:
                                    triallist.append([k, self.rlist[self.llist.index(j)]])
                            if len(triallist) == len(clearlist):
                                for n in triallist:
                                    if triallist.index(n) == 0:
                                        self.nerlist.append((n[0], "b-" + n[1]))
                                    elif triallist.index(n) == len(triallist) - 1:
                                        self.nerlist.append((n[0], "i-" + n[1]))
                                    elif triallist.index(n) != 0 and triallist.index(n) != -1:
                                        self.nerlist.append((n[0], n[1]))
                                var = len(clearlist) - 1
                                break
                            else:
                                self.nerlist.append((i, self.rlist[self.llist.index(j)]))
                                break
                        elif count == len(self.llist):
                             self.nerlist.append((i, "out"))
        return self.nerlist
