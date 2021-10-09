def polyn(s):

    return s == s[::-1]



def extension(s):

    n = s.split('.')

    if len(n) < 2:
        return 'invalid'
    else:
        return n[len(n) - 1]

print(extension('jjjjjjj.pe.df'))

def time(s):
    t = []

    t.append(s//(60*60*24))
    s = s % (60*60*24)
    t.append(s//(60*60))
    s = s % (60*60)
    t.append(s//60)
    
    date = ':'.join(map(str,t))

    return date

print(time(8648364800))


def three(s):

    s = str(s)
    
    return int(s) + int(s*2) + int(s*3)

print(three(5))


def maimum(s):

    k = s[0]

    for i in range(len(s) - 1):
        if k < s[i]:
            j = s[i]
            s[i] = k
            k = j