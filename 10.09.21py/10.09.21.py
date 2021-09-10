import string

# print(string.ascii_letters)

# a = []

# for i in string.ascii_letters :
#    a.append(i) 

# print(a)

# j = 0
# b = []
# while j < len(string.ascii_letters):
#     b.append(string.ascii_letters[j])
#     j+=1

# print(b)

# c = list(string.ascii_letters)

# print(c)


# for i in c:
#     print(i)

# i = 0
# while i < len(c):
#     print(c[i])
#     i += 1



def show(func):
    def new_fuunc(*args, **kwargs):
        print('running function:', func.__name__)
        print('positional arguments are', args)
        result = func(*args,**kwargs)
        print('Keyword arguments are:', kwargs)
        print('Result', result)
        return result
    return new_fuunc


@show
def sum_(a,b):
    return a + b

sum_(5,8)
