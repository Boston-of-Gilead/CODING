#https://www.codewars.com/kata/check-for-prime-numbers/train/python

def is_prime(n):
    num = n
    if num > 1 and num != 2:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    elif num == 2:
        return True
    else:
        return False
