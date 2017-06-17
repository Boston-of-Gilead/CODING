#https://www.codewars.com/kata/leonardo-dicaprio-and-oscars/train/python

def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar == 87 or oscar < 86:
        return "When will you give Leo an Oscar?"
    elif oscar > 99:
        return "Leo got one already!"
    else:
        return False
    pass