import string

# def text(s):
#     cnt = {}
#     for i in string.ascii_letters:
#         cnt[i] = s.count(i)
#     return cnt

# print(text('gfgfgfgfgf'))

# name = ['efdd', 'dfdffd', 'fkdjfmkd', 'dfkjdkm']

# city =[{200,123233}, {28660,656233}, {76767800,126533}, {288780,12365673}]
# def inf_city(n,r):
#     inf = {
#         'count': n,
#         'size': r + 'км^2'
#     }

#     return inf

# def reg(n,c):
#     d = {}
#     for n,c in zip(n,c):
#         d[n] = c

#     return d

# print(reg(name,city))

# set_1 = {1,2,3,4,5,6}
# set_2 = {1,6,7,8,9,0}

# print(set_1.isdisjoint(set_2))
# print(set_1 == set_2)
# print(set_1 <= set_2)
# print(set_1 >= set_2)
# print(set_1.union(set_2))
# print(set_1.intersection(set_2))
# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))
# print(set_1.symmetric_difference(set_2))
# print(set_1.copy())
l = [2,34,3,34,34,3,43,4,5,45,45,4,45,4,64,6,46,56,24,6,7]
l2 = [2,3,34,34,4,5,45,45,656,24,6,7,8,343443,8676]
def unique(array):
    set_1 = set(array)
    list_1 = list(set_1)

    return list_1

print("Список уникальных значений:", unique(l))

def intersection(list_1, list_2):

    return list(set(list_1) & set(list_2))


print('Список пересекающихся элементов:',intersection(l, l2))

