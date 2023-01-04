text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)

print(f(text_list[1]))

print(list(map(f, text_list)))

print(list(map(lambda x: len(x), text_list)))
