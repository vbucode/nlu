#class Classification

classlist = []
llist = []
rlist = []

with open("classes.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)
class Classificator:
    def __init__(self, text):
        self.text = text
    def load(self):
        for i in self.text:
            flag = 1
            for j in llist:
                if i == j:
                    classlist.append(rlist[llist.index(j)])
                    flag = 0
            if flag != 0:
                classlist.append(i)
        return classlist
