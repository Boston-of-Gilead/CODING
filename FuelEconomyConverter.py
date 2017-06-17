#https://www.codewars.com/kata/miles-per-gallon-to-kilometers-per-liter/train/python

def converter(mpg):
    kpg = mpg * 1.609344
    kpl = kpg / 4.54609188
    kpl = round(kpl, 2)
    return kpl