import string
from random import choice

def random_string(num):

    s = ''

    for i in range(num):

        s += choice(string.ascii_letters)

    #print(s)
    return s

# print(random_string(6))

def string_max(s):
    j = 0
    for i in s:

        if i.isupper():
            j += 1
    
    if (len(s) - j) < j:
        return 1
    elif j == 0  or (len(s) - j) == j:
        return -1
    else:
        return 0


#print(string_max('jgjJNJ'))

def string_list(lenght,num):
    result = [random_string(lenght) for i in range(num)]

    return result

#print(string_list(5,6))


def string_percent(s):

    low = 0
    up = 0
    count_low = 0
    count_up = 0
    count_equally = 0

    for i in s:
        j = 0
        for k in i:

            if k.isupper():
                j += 1
        
        up += j
        low += len(i) - j

        if (len(i) - j) < j:
            count_up +=1
        elif j == 0  or (len(i) - j) == j:
            count_equally +=1
        else:
            count_low += 1

    print('quantity cap > low =', count_up / (len(s) / 100),'%')
    print('quantity cap < low =', count_low / (len(s) / 100),'%')
    print('quantity equally =', count_equally / (len(s) / 100),'%')
    print('capital letters:', up / ((up + low)/100),'%')
    print('lowercase letters:', low / ((up + low)/100),'%')

string_percent(string_list(5,19))