import os

files = [r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S03 - rozbudowa kodu\PLIKI\S03 - 1.txt",
         r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S03 - rozbudowa kodu\PLIKI\S03 - 2.txt"]

with open(files[0], "r") as file:
    print(os.path.basename((files[0])))
    exec(file.read())


with open(files[1], "r") as file:
    print(os.path.basename((files[1])))
    exec(file.read())
