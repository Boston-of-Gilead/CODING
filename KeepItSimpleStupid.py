#https://www.codewars.com/kata/kiss-keep-it-simple-stupid/train/python

def is_kiss(words):
    word_count = len(words.split())

    letter_count = map(len, words.split())

    if any(x > word_count for x in letter_count):
        return 'Keep It Simple Stupid'
    else:
        return 'Good work Joe!'
