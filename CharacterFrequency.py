#https://www.codewars.com/kata/character-frequency-2/train/python

def char_freq(message):
    letterdict={}
    for letter in message:
        letterdict[letter] = 0
    for letter in message:
        letterdict[letter] += 1
    return letterdict
    pass