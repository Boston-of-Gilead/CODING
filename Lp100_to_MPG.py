#https://www.codewars.com/kata/fuel-economy-converter-mpg-l-slash-100-km/train/python

def mpg2lp100km(mpg):
    # mile = km * 1.609344
    # 100km = 62.1371 miles
    # gal = l * 3.785411784
    answer = ((62.1371/mpg)*3.785411784)
    answer = (round(answer, 2))
    return answer
    
def lp100km2mpg(lp100km):
    #lp100km = int(lp100km)
    #(lp100/3.785411784)=gal per 100km= g100. 62.1371/g100=mpg
    g100 = (lp100km/3.785411784)
    answer = (62.1371/g100)
    answer = (round(answer, 2))
    return answer
