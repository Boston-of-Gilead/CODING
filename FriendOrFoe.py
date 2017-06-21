#https://www.codewars.com/kata/friend-or-foe/train/python

def friend(x):
    ind = []
    for y in x:
        if len(y) == 4:
            ind.append(y)           
        else:
            pass
    return ind
