def number2words(n):
    d = {'0':'zero', '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six', '7': 'seven',
         '8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
         '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty',
         '60':'sixty','70':'seventy','80':'eighty','90':'ninety','100':'one hundred','1000':'one thousand'}
    mystr = str(n)
    if mystr in d.keys():
        return d[mystr]
    elif n<100:
        return d[str(n-(n%10))] + '-' + d[str(n%10)] 
    elif n<1000:
        divide = str(n/100)
        if n%100 == 0:
            return d[divide[0]] +' '+ 'hundred'
        else:
            mymod = n%100
            return d[divide[0]] + ' '+ 'hundred' + ' ' +number2words(mymod)
    elif n<10000:
        divide = str(n/1000)
        if n%1000 == 0:
            return d[divide[0]] + ' ' + 'thousand'
        else:
            mymod = n%1000
            return d[divide[0]] + ' '+ 'thousand' + ' ' +number2words(mymod)
    else:
        divide = str(n//1000)
        if n%1000 == 0:
            return number2words(int(divide)) + ' ' + 'thousand'
        else:
            mymod = n%1000
            return number2words(int(divide)) + ' '+ 'thousand' + ' ' +number2words(mymod)
    
