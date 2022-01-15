#returns the next lower number using the same digits
#if number is already the lowest, returns None
def next_lower(n):
    sort = sorted(list(str(n)))
    sort2 = "".join(sort)
    lowest = int(sort2)
    if lowest == n:
        return -1
    first = 0
    second = 0
    if sort2[0] == 0:
        first = sort2[0]
        second = sort2[1]
        sort2[0] = second
        sort2[1] = first
    for x in reversed(range(lowest,n)):
        if sorted(list(str(x))) == sort:
            return x
