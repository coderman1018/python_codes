def high(x):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words = x.split()
    score = 0
    word = ''
    for x in words:
        current = 0
        for y in x:
            current += letters.index(y)+1
        if current>score:
            score = current
            word = x
    return word
