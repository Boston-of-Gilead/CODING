#https://www.codewars.com/kata/multiply-the-number/train/python

def multiply(n):
    x = str(n)
    for char in '-':
        x = x.replace(char,'') 
    length = len(x)
    exp = int(length)
    factor = 5 ** exp
    result = n * factor
    return result
