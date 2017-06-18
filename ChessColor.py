#https://www.codewars.com/kata/white-or-black/train/python

def mine_color(line, number):
    white_rows = 'aceg'
    black_rows = 'bdfh'
    
    if line in black_rows:
        if number % 2 != 0:
            return 'white'
        else:
            return 'black'
    if line in white_rows:
        if number % 2 != 0:
            return 'black'
        else:
            return 'white'

