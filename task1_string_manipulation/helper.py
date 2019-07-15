
def removeMultyOccurence(str):
    temp = ""

    for s in str:
        if s.lower() not in temp.lower():
            temp = temp + s

    return temp

def repeats(str, ch):
    count = 0
    for s in str:
        if s.lower() == ch.lower():
            count = count + 1

    if count>1:
        return True
    else:
        return False

def removeFirst(str, ch):

    index = str.find(ch)


    if index == 0:
        str = str[1:]
    elif index == len(str) - 1:
        str = str[0: len(str)-1]
    else:
        str = str[0:index] + str[index+1: len(str)]

    return str





def removeFirstOccurence(str):
    temp = ""
    list = []
    for s in str:
        if repeats(str, s) == True\
                and s.lower() not in list:
            temp = removeFirst(str,s)
            list.append(s.lower())
            str = temp

    return temp

print(removeFirstOccurence('TechTeam'))