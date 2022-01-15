#returns 13th letter for each letter in a string
def rot13(message):
    letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    big_letters = letters.upper()
    final = []
    for x in message:
        if x in letters:
            final.append(letters[letters.index(x)+13])
        elif x in big_letters:
            final.append(big_letters[big_letters.index(x)+13])
        else:
            final.append(x)
    return "".join(final)
