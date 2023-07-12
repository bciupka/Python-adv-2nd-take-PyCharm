import os
import itertools


def scantree(path):
    for i in os.scandir(path):
        if i.is_dir():
            yield i
            yield from scantree(i.path)
        elif not i.is_dir():
            yield i


path = r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S10 - generatory"
listening = (i for i in scantree(path))

data = []
for i in listening:
    data.append({"Name" : i.name, "Type" : ("Catalog" if i.is_dir() else "File")})

for i in data:
    print(i)

x = sorted(data, key=lambda y: y["Type"])
for i, y in itertools.groupby(x, key=lambda y: y["Type"]):
    print(i, list(y))