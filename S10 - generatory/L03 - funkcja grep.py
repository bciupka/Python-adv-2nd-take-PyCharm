import os
import requests


def gen_get_files(dir):
    for i in os.listdir(dir):
        yield os.path.join(dir, i)

def gen_get_file_lines(filename):
    with open(filename, "r") as file:
        for i in file:
            yield i.rstrip("\n")

def check_webpage(url):
    try:
        temp = requests.get(url)
    except:
        return False

    if temp.status_code == 200:
        return True
    else:
        return False

try:
    os.mkdir(r".\PLIKI\links")
except:
    pass

with open(r".\PLIKI\LINKS\pl.txt", 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r".\PLIKI\LINKS\com.txt", 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

file = gen_get_files(r".\PLIKI\links")

for i in file:
    for j in gen_get_file_lines(i):
        print(j, check_webpage(j))