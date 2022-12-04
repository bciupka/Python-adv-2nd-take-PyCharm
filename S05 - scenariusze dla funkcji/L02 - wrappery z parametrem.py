import functools
import os

def wrapper(action, path):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            with open(path, "a") as f:
                f.write("{} in location {}".format(action, args[0]))
                f.write("\n")
            return func(*args, **kwargs)
        return wrapper2
    return wrapper1


@wrapper("FILE CREATE", r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S05 - scenariusze dla funkcji\PLIKI\log.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper("FILE DELETE", r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S05 - scenariusze dla funkcji\PLIKI\log.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)

create_file(r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S05 - scenariusze dla funkcji\PLIKI\file.txt")
delete_file(r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S05 - scenariusze dla funkcji\PLIKI\file.txt")