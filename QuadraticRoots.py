#https://www.codewars.com/kata/find-the-sum-of-the-roots-of-a-quadratic-equation/train/python

def roots(a,b,c):
    import math

    b2 = b**2
    r = ((b**2)-(4*a*c))
    if r < 0:
        return None
    else:
        ra = math.sqrt(r)
        di = a * 2

        x1 = ((-b)+ ra)/di
        x2 = ((-b)- ra)/di
        sum = x1 + x2
        sum_round = round(sum,2)
        return sum_round
