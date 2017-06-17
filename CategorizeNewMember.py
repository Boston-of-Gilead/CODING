def openOrSenior(data):
    output = []
    for x in data:
        if x[0]>=55 and x[1]>=8:
            output.append('Senior')
        else:
            output.append('Open')
    return output
