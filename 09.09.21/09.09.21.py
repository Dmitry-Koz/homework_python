from random import randrange


# name = 'Kojewnikov Dmitry Aleksandrovich'

# def rename(s) :
#     start = 0
#     names = []
#     for i in range(len(s)):
#         if s[i] == ' ':
#             names.append(s[start:i])
#             start = i + 1
#         if i == len(s) - 1:
#             names.append(s[start:i])
    
#     return names[0] + ' ' + names[1][0:1] + '.' + names[2][0:1] + '.'

# print(rename(name))


# name = ['Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich']

# def rename(s) :

#     result = []
#     names = []

#     for i in range(len(s)):

#         names = s[i].split(' ')
#         result.append(names[0] + ' ' + names[1][0:1] + '.' + names[2][0:1] + '.')

#     return result

# print(rename(name))


# name = ['Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich','Kojewnikov Dmitry Aleksandrovich']

# def rename(s) :
    
#     names = s.split(' ')
    
#     return names[0] + ' ' + names[1][0:1] + '.' + names[2][0:1] + '.'


# def rename_more(s):
#     # result = []

#     # for n in s:
#     #     new_name = rename(n)
#     #     result.append(new_name)

#     result = [rename(n) for n in s]

#     return result



# print(rename_more(name))


# 1) функция которая размножает имена 

def generate(numb,name):

    result = [name for i in range(0,numb)]

    return result

print(generate(10, 'Kojewnikov D.A.'))


# 2) генератор имен (generator(gild))

def pro_generate(numb = 4):

    i = 0
    result = []

    while i <= numb: #Quantity fio

        fio = ''

        for j in range(0,3):

            fio += chr(randrange(65,90))
            name = ['' + chr(randrange(97,122)) for k in range(randrange(3,7)) ] #different characters
            fio += ''.join(name) #determine the number of characters

            if j < 2 :
                fio += ' '

        result.append(fio)
        i += 1
    return result

print(pro_generate(5))



    


