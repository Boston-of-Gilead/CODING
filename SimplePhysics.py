#https://www.codewars.com/kata/simple-physics-problem/train/python

def solveit(vi, vf, t):
    a = (vf-vi)/t
    d = vi*t + 0.5*a*(t**2)
    a = round(a,2)
    d = round(d,2)
    
    if vi > vf:
        return []
    else:
        return [a,d]
