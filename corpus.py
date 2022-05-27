
def ner():
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
    return llist, rlist
