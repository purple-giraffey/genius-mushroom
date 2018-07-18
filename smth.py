#Numbers Factory
def chekjo(numb):
    numbr = numb
    x = []
    d = ""
    while numbr%2 == 0:
        numbr = int(numbr/2)
        x.append(2)
    while numbr%3 == 0:
        numbr = int(numbr/3)
        x.append(3)
    while numbr%5 == 0:
        numbr = int(numbr/5)
        x.append(5)
    while numbr%7 == 0:
        numbr = int(numbr/7)
        x.append(7)
        print x
    while x.count(2)>1:
        x.append(4)
        x.remove(2)
        x.remove(2)
    while 2 in x and 4 in x:
        x.remove(2)
        x.remove(4)
        x.append(8)
        print x
    while 2 in x and 3 in x:
        x.remove(2)
        x.remove(3)
        x.append(6)
        print x
    while x.count(3)>1 and x.count(3)%2==0:
        x.append(9)
        x.remove(3)
        x.remove(3)
        print x
        print numbr
    if numbr>1:
        return 0
    if x == []:
        return 0
    x = sorted(x)
    for xd in x:
        d = d + str(xd)
    return int(d)
    

print chekjo(1024)