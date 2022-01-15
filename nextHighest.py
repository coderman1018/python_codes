#returns the next highest number formed by using the same digits. 
#if number is already the highest, returns None
def next_highest(n):
    sort = sorted(list(str(n)))
    sort2 = "".join(sort)
    highest = int(sort2[::-1])
    for x in range(n+1,highest+1):
        if sorted(list(str(x))) == sort:
            return x
