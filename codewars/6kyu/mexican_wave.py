def wave(people):return [people[:x]+people[x:x+1].upper()+people[x+1:] for x in range(len(people)) if people[x]!=' ']
